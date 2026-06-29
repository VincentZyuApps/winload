#!/usr/bin/env node

/**
 * 📦 winload npm CLI entry point.
 *
 * 🚀 This launcher is shared by the Rust binary npm distribution.
 * 🧭 Users can install it in three ways:
 *   - npm install -g @vincentzyuapps/winload
 *   - npm install -g winload-rust-bin
 *   - npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
 *
 * 🔎 It resolves the current platform package and forwards all CLI arguments to
 * the precompiled Rust binary.
 */

"use strict";

const { spawnSync } = require("child_process");
const { getBinaryPath } = require("./index.js");

const bin = getBinaryPath();

// Show implementation info for help & version flags
const args = process.argv.slice(2);
if (args.includes("--help") || args.includes("-h") || args.includes("--version") || args.includes("-V")) {
  console.error("ℹ️  This is the Rust binary edition (installed from npm)\n");
}

const result = spawnSync(bin, args, {
  stdio: "inherit",
  windowsHide: false,
});

process.exit(result.status ?? 1);
