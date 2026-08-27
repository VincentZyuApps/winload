// Owns mutable application state, traffic collection, and device navigation.

use crate::collector::{Collector, DeviceInfo};
use crate::config::{BarStyle, GraphStyle, MaxMode, RunConfig, TitleAlign, Unit, XAxis, YAxis};
use crate::i18n::t;
use crate::loopback::{LoopbackCapture, LoopbackCounters, LoopbackMode};
use crate::stats::StatisticsEngine;

pub struct DeviceView {
    pub info: DeviceInfo,
    pub engine: StatisticsEngine,
}

pub struct App {
    pub views: Vec<DeviceView>,
    pub current_idx: usize,
    pub title: Option<String>,
    pub title_align: TitleAlign,
    pub emoji: bool,
    pub unicode: bool,
    pub unit: Unit,
    pub bar_style: BarStyle,
    pub in_color: ratatui::style::Color,
    pub out_color: ratatui::style::Color,
    pub max_mode: MaxMode,
    pub max_half_life: f64,
    pub max_y_value: Option<f64>,
    pub no_graph: bool,
    pub hide_separator: bool,
    pub no_color: bool,
    pub interval: u64,
    pub average: u64,
    pub show_debug: bool,
    pub graph_style: GraphStyle,
    pub x_axis: XAxis,
    pub last_x_axis_interval: u64,
    pub y_axis: YAxis,
    pub loopback_mode: LoopbackMode,
    pub loopback_info: Option<String>,
    pub loopback_counters: Option<LoopbackCounters>,
    pub loopback_capture: Option<LoopbackCapture>,
    collector: Collector,
}

impl App {
    pub fn new(config: RunConfig) -> Self {
        let collector = Collector::new(config.netlink);
        let smart_half_life = (config.max_mode == MaxMode::Smart).then_some(config.max_half_life);
        let views: Vec<_> = collector
            .devices()
            .into_iter()
            .map(|info| DeviceView {
                info,
                engine: StatisticsEngine::new(config.interval, config.average, smart_half_life),
            })
            .collect();
        let current_idx = config
            .device
            .as_ref()
            .and_then(|name| {
                let name = name.to_lowercase();
                views
                    .iter()
                    .position(|view| view.info.name.to_lowercase().contains(&name))
            })
            .unwrap_or(0);
        let loopback_mode = if config.npcap {
            LoopbackMode::Npcap
        } else {
            LoopbackMode::None
        };
        let last_x_axis_interval = config.x_axis.interval().unwrap_or(5);
        Self {
            views,
            current_idx,
            title: config.title,
            title_align: config.title_align,
            emoji: config.emoji,
            unicode: config.unicode,
            unit: config.unit,
            bar_style: config.bar_style,
            in_color: config.in_color,
            out_color: config.out_color,
            max_mode: config.max_mode,
            max_half_life: config.max_half_life,
            max_y_value: config.max_y_value,
            no_graph: config.no_graph,
            hide_separator: config.hide_separator,
            no_color: config.no_color,
            interval: config.interval,
            average: config.average,
            show_debug: false,
            graph_style: config.graph_style,
            x_axis: config.x_axis,
            last_x_axis_interval,
            y_axis: config.y_axis,
            loopback_mode,
            loopback_info: None,
            loopback_counters: None,
            loopback_capture: None,
            collector,
        }
    }

    pub fn current_view(&self) -> Option<&DeviceView> {
        self.views.get(self.current_idx)
    }

    pub fn update(&mut self) {
        let mut snapshots = self.collector.collect();
        if let Some(counters) = &self.loopback_counters {
            let elapsed = self.collector.elapsed_secs();
            for (name, snapshot) in &mut snapshots {
                if name.to_lowercase().contains("loopback") {
                    snapshot.bytes_recv = counters.get_recv();
                    snapshot.bytes_sent = counters.get_sent();
                    snapshot.elapsed_secs = elapsed;
                }
            }
        }
        for view in &mut self.views {
            if let Some(snapshot) = snapshots.get(&view.info.name) {
                view.engine.update(snapshot.clone());
            }
        }
    }

    pub fn next_device(&mut self) {
        if !self.views.is_empty() {
            self.current_idx = (self.current_idx + 1) % self.views.len();
        }
    }
    pub fn prev_device(&mut self) {
        if !self.views.is_empty() {
            self.current_idx = (self.current_idx + self.views.len() - 1) % self.views.len();
        }
    }
    pub fn cycle_graph_style(&mut self) {
        if !self.no_graph {
            self.graph_style = self.graph_style.next();
        }
    }
    pub fn toggle_x_axis(&mut self) {
        if !self.no_graph {
            self.x_axis = match self.x_axis {
                XAxis::None => XAxis::Seconds(self.last_x_axis_interval),
                XAxis::Seconds(value) => {
                    self.last_x_axis_interval = value;
                    XAxis::None
                }
            };
        }
    }
    pub fn cycle_y_axis(&mut self) {
        if !self.no_graph {
            self.y_axis = self.y_axis.next();
        }
    }

    pub fn exit_info(&self) -> String {
        let prefix = if self.emoji {
            t("exit_platform_emoji")
        } else {
            t("exit_platform")
        };
        #[cfg(target_os = "windows")]
        {
            return format!(
                "{prefix} Npcap: {}",
                if self.loopback_mode == LoopbackMode::Npcap {
                    t("on")
                } else {
                    t("off")
                }
            );
        }
        #[cfg(any(target_os = "android", target_os = "linux"))]
        {
            return format!(
                "{prefix} {}: {}",
                t("network_label"),
                if self.collector.using_netlink() {
                    t("netlink_mode")
                } else {
                    t("sysinfo_default")
                }
            );
        }
        #[allow(unreachable_code)]
        String::new()
    }
}
