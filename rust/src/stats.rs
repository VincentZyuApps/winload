//! 流量统计引擎
//! 维护滑动窗口，计算 Cur / Avg / Min / Max / Ttl 五项指标。

use std::collections::VecDeque;

use crate::collector::Snapshot;

/// 某一方向（收/发）的统计结果
#[derive(Clone, Debug)]
pub struct TrafficStats {
    /// 当前速率 (bytes/s)
    pub current: f64,
    /// 平均速率 (bytes/s)
    pub average: f64,
    /// 最小速率 (bytes/s)
    pub minimum: f64,
    /// 最大速率 (bytes/s)
    pub maximum: f64,
    /// 累计字节数
    pub total: u64,
}

impl Default for TrafficStats {
    fn default() -> Self {
        Self {
            current: 0.0,
            average: 0.0,
            minimum: f64::INFINITY,
            maximum: 0.0,
            total: 0,
        }
    }
}

/// 统计引擎：为单个网卡维护收发两个方向的统计数据
pub struct StatisticsEngine {
    samples: VecDeque<Snapshot>,
    second_window: usize,
    max_samples: usize,
    sample_count: usize,

    /// 收方向统计
    pub incoming: TrafficStats,
    /// 发方向统计
    pub outgoing: TrafficStats,

    /// 收方向速率历史 (front = 最新值，供图形绘制)
    pub incoming_history: VecDeque<f64>,
    /// 发方向速率历史
    pub outgoing_history: VecDeque<f64>,
}

impl StatisticsEngine {
    pub fn new(refresh_interval_ms: u64, average_window_sec: u64) -> Self {
        let second_window = (1000u64 / refresh_interval_ms).max(1) as usize;
        let max_samples =
            ((1000u64 / refresh_interval_ms) * average_window_sec).max(600) as usize;

        Self {
            samples: VecDeque::with_capacity(max_samples),
            second_window,
            max_samples,
            sample_count: 0,
            incoming: TrafficStats::default(),
            outgoing: TrafficStats::default(),
            incoming_history: VecDeque::with_capacity(1024),
            outgoing_history: VecDeque::with_capacity(1024),
        }
    }

    /// 喂入新的采样快照，重新计算统计
    pub fn update(&mut self, snapshot: Snapshot) {
        self.samples.push_back(snapshot);
        if self.samples.len() > self.max_samples {
            self.samples.pop_front();
        }
        self.sample_count += 1;

        let n = self.samples.len();
        if n < 2 {
            return;
        }

        let latest = &self.samples[n - 1];

        // ── 当前速率 (最近 ~1s 的窗口) ──
        let sec_idx = if n > self.second_window + 1 {
            n - 1 - self.second_window
        } else {
            0
        };
        let older = &self.samples[sec_idx];
        let dt = latest.elapsed_secs - older.elapsed_secs;

        if dt > 0.0 {
            self.incoming.current =
                ((latest.bytes_recv as f64 - older.bytes_recv as f64) / dt).max(0.0);
            self.outgoing.current =
                ((latest.bytes_sent as f64 - older.bytes_sent as f64) / dt).max(0.0);
        }

        // 记录到历史 (graph 用)
        if self.incoming_history.len() >= 1024 {
            self.incoming_history.pop_back();
        }
        if self.outgoing_history.len() >= 1024 {
            self.outgoing_history.pop_back();
        }
        self.incoming_history.push_front(self.incoming.current);
        self.outgoing_history.push_front(self.outgoing.current);

        // ── 平均速率 (整个窗口) ──
        let oldest = &self.samples[0];
        let dt_all = latest.elapsed_secs - oldest.elapsed_secs;
        if dt_all > 0.0 {
            self.incoming.average =
                ((latest.bytes_recv as f64 - oldest.bytes_recv as f64) / dt_all).max(0.0);
            self.outgoing.average =
                ((latest.bytes_sent as f64 - oldest.bytes_sent as f64) / dt_all).max(0.0);
        }

        // ── Min / Max ──
        if self.incoming.current > 0.0 || self.outgoing.current > 0.0 || self.sample_count > 3 {
            self.incoming.minimum = self.incoming.minimum.min(self.incoming.current);
            self.incoming.maximum = self.incoming.maximum.max(self.incoming.current);
            self.outgoing.minimum = self.outgoing.minimum.min(self.outgoing.current);
            self.outgoing.maximum = self.outgoing.maximum.max(self.outgoing.current);
        }

        // 修正 infinity
        if self.incoming.minimum == f64::INFINITY {
            self.incoming.minimum = 0.0;
        }
        if self.outgoing.minimum == f64::INFINITY {
            self.outgoing.minimum = 0.0;
        }

        // ── Total ──
        self.incoming.total = latest.bytes_recv;
        self.outgoing.total = latest.bytes_sent;
    }
}

// ─── 格式化工具函数 ───────────────────────────────────────

/// 将 bytes/s 转为人类可读的 Bit/s 格式
pub fn format_speed(bytes_per_sec: f64) -> String {
    let bits = bytes_per_sec * 8.0;
    if bits >= 1024.0 * 1024.0 * 1024.0 {
        format!("{:.2} GBit/s", bits / (1024.0 * 1024.0 * 1024.0))
    } else if bits >= 1024.0 * 1024.0 {
        format!("{:.2} MBit/s", bits / (1024.0 * 1024.0))
    } else if bits >= 1024.0 {
        format!("{:.2} kBit/s", bits / 1024.0)
    } else {
        format!("{:.2} Bit/s", bits)
    }
}

/// 将字节数转为人类可读格式
pub fn format_bytes(total_bytes: u64) -> String {
    let b = total_bytes as f64;
    if b >= 1024.0 * 1024.0 * 1024.0 {
        format!("{:.2} GByte", b / (1024.0 * 1024.0 * 1024.0))
    } else if b >= 1024.0 * 1024.0 {
        format!("{:.2} MByte", b / (1024.0 * 1024.0))
    } else if b >= 1024.0 {
        format!("{:.2} kByte", b / 1024.0)
    } else {
        format!("{:.2} Byte", b)
    }
}
