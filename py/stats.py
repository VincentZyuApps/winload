"""
stats.py - 流量统计引擎
维护滑动窗口，计算 Cur / Avg / Min / Max / Ttl 五项指标。
"""

from collections import deque
from dataclasses import dataclass
from typing import Optional

from collector import Snapshot


@dataclass
class TrafficStats:
    """某一方向（收/发）的统计结果"""
    current: float = 0.0     # 当前速率 (bytes/s)
    average: float = 0.0     # 平均速率 (bytes/s)
    minimum: float = float("inf")   # 最小速率 (bytes/s)
    maximum: float = 0.0     # 最大速率 (bytes/s)
    total: int = 0           # 累计字节数


class StatisticsEngine:
    """
    为单个网卡维护收发两个方向的统计数据。
    滑动窗口保存历史快照，据此计算各项指标。
    """

    def __init__(
        self,
        refresh_interval_ms: int = 500,
        average_window_sec: int = 300,
    ):
        self._refresh_ms = refresh_interval_ms
        self._avg_window_sec = average_window_sec

        # 滑动窗口
        max_samples = max(
            int(1000 / refresh_interval_ms * average_window_sec), 600
        )
        self._samples: deque[Snapshot] = deque(maxlen=max_samples)

        # 计算 1 秒窗口需要的样本数
        self._second_window = max(int(1000 / refresh_interval_ms), 1)

        # 统计结果
        self.incoming = TrafficStats()
        self.outgoing = TrafficStats()

        # 用于记录本次速率的历史（供 graph 使用）
        self._incoming_history: deque[float] = deque(maxlen=1024)
        self._outgoing_history: deque[float] = deque(maxlen=1024)

        self._first_snapshot: Optional[Snapshot] = None

    @property
    def incoming_history(self) -> deque:
        return self._incoming_history

    @property
    def outgoing_history(self) -> deque:
        return self._outgoing_history

    def update(self, snapshot: Snapshot) -> None:
        """喂入新的采样快照，重新计算统计"""
        self._samples.append(snapshot)
        if self._first_snapshot is None:
            self._first_snapshot = snapshot

        n = len(self._samples)
        if n < 2:
            return

        latest = self._samples[-1]

        # --- 当前速率 (最近 ~1s 的窗口) ---
        sec_idx = max(0, n - 1 - self._second_window)
        older = self._samples[sec_idx]
        dt = latest.timestamp - older.timestamp
        if dt > 0:
            cur_in = (latest.bytes_recv - older.bytes_recv) / dt
            cur_out = (latest.bytes_sent - older.bytes_sent) / dt
        else:
            cur_in = cur_out = 0.0

        self.incoming.current = max(cur_in, 0.0)
        self.outgoing.current = max(cur_out, 0.0)

        # 记录到历史（供 graph）
        self._incoming_history.appendleft(self.incoming.current)
        self._outgoing_history.appendleft(self.outgoing.current)

        # --- 平均速率 (整个窗口) ---
        oldest = self._samples[0]
        dt_all = latest.timestamp - oldest.timestamp
        if dt_all > 0:
            self.incoming.average = max(
                (latest.bytes_recv - oldest.bytes_recv) / dt_all, 0.0
            )
            self.outgoing.average = max(
                (latest.bytes_sent - oldest.bytes_sent) / dt_all, 0.0
            )

        # --- Min / Max ---
        if self.incoming.current > 0 or self.outgoing.current > 0 or n > 3:
            self.incoming.minimum = min(
                self.incoming.minimum, self.incoming.current
            )
            self.incoming.maximum = max(
                self.incoming.maximum, self.incoming.current
            )
            self.outgoing.minimum = min(
                self.outgoing.minimum, self.outgoing.current
            )
            self.outgoing.maximum = max(
                self.outgoing.maximum, self.outgoing.current
            )

        # 修正 inf
        if self.incoming.minimum == float("inf"):
            self.incoming.minimum = 0.0
        if self.outgoing.minimum == float("inf"):
            self.outgoing.minimum = 0.0

        # --- Total ---
        if self._first_snapshot:
            self.incoming.total = latest.bytes_recv
            self.outgoing.total = latest.bytes_sent


def format_speed(bytes_per_sec: float) -> str:
    """将 bytes/s 转为人类可读的 Bit/s 格式"""
    bits = bytes_per_sec * 8
    units = [
        (1024 ** 3, "GBit/s"),
        (1024 ** 2, "MBit/s"),
        (1024,      "kBit/s"),
        (1,         "Bit/s"),
    ]
    for threshold, unit in units:
        if bits >= threshold:
            return f"{bits / threshold:.2f} {unit}"
    return "0.00 Bit/s"


def format_bytes(total_bytes: int) -> str:
    """将字节数转为人类可读格式"""
    b = float(total_bytes)
    units = [
        (1024 ** 3, "GByte"),
        (1024 ** 2, "MByte"),
        (1024,      "kByte"),
        (1,         "Byte"),
    ]
    for threshold, unit in units:
        if b >= threshold:
            return f"{b / threshold:.2f} {unit}"
    return "0.00 Byte"
