use std::process::Command;

fn main() {
    let target = std::env::var("TARGET").unwrap();
    println!("cargo:rustc-env=TARGET={target}");
    emit_git_build_info();

    // Windows MSVC + npcap feature: delay-load wpcap.dll
    // Without this, the binary fails to start on machines without Npcap installed,
    // because the OS loader cannot find wpcap.dll at process startup.
    // With /DELAYLOAD, wpcap.dll is only loaded when pcap functions are first called
    // (i.e., only when --npcap flag is used at runtime).
    if target.contains("windows-msvc") && cfg!(feature = "npcap") {
        println!("cargo:rustc-link-lib=delayimp");
        println!("cargo:rustc-link-arg=/DELAYLOAD:wpcap.dll");
    }

    // Note: xp_shim.c (MinGW GetFileInformationByHandleEx compat) was removed
    // as Rust 1.77+ requires Windows 10+ for all targets.
}

fn emit_git_build_info() {
    println!("cargo:rerun-if-changed=../.git/HEAD");
    if let Some(head_ref) = git_output(&["symbolic-ref", "-q", "HEAD"]) {
        if let Some(ref_path) = git_output(&["rev-parse", "--git-path", head_ref.as_str()]) {
            println!("cargo:rerun-if-changed={ref_path}");
        }
    }

    let commit_hash = git_output(&["rev-parse", "--short=7", "HEAD"])
        .unwrap_or_else(|| "unknown".to_string());
    let commit_time = git_output(&["show", "-s", "--format=%cI", "HEAD"])
        .unwrap_or_else(|| "unknown".to_string());

    println!("cargo:rustc-env=WINLOAD_GIT_COMMIT_HASH={commit_hash}");
    println!("cargo:rustc-env=WINLOAD_GIT_COMMIT_TIME={commit_time}");
}

fn git_output(args: &[&str]) -> Option<String> {
    let output = Command::new("git").args(args).output().ok()?;
    if !output.status.success() {
        return None;
    }
    let value = String::from_utf8(output.stdout).ok()?.trim().to_string();
    if value.is_empty() {
        None
    } else {
        Some(value)
    }
}
