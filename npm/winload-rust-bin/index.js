/**
 * 📦 winload npm binary path resolver.
 *
 * 🧭 The npm release is available as:
 *   - @vincentzyuapps/winload on npm
 *   - winload-rust-bin on npm
 *   - @vincentzyuapps/winload on GitHub Packages
 *
 * 🧩 optionalDependencies use each platform package's os/cpu fields, so npm only
 * installs the package matching the current machine. This module locates that
 * platform package and returns the bundled Rust binary path.
 *
 * 🛠 This follows the same packaging pattern used by projects such as esbuild,
 * @biomejs/biome, and turbo.
 */

"use strict";

const path = require("path");

/**
 * 🗺 Platform package mapping.
 * key:   `${process.platform}-${process.arch}`
 * value: npm platform package name
 */
const PLATFORMS = {
  "win32-x64":    "@vincentzyuapps/winload-win32-x64",
  "win32-arm64":  "@vincentzyuapps/winload-win32-arm64",
  "linux-x64":    "@vincentzyuapps/winload-linux-x64",
  "linux-arm64":  "@vincentzyuapps/winload-linux-arm64",
  "darwin-x64":   "@vincentzyuapps/winload-darwin-x64",
  "darwin-arm64":  "@vincentzyuapps/winload-darwin-arm64",
};

/**
 * 🔎 Resolve the absolute path to the winload binary for the current platform.
 * @returns {string} Binary path
 * @throws {Error} Unsupported platform or missing platform package
 */
function getBinaryPath() {
  const key = `${process.platform}-${process.arch}`;
  const pkg = PLATFORMS[key];

  if (!pkg) {
    const supported = Object.keys(PLATFORMS).join(", ");
    throw new Error(
      `winload: unsupported platform "${key}"\n` +
      `Supported: ${supported}\n` +
      `Download manually: https://github.com/VincentZyuApps/winload/releases`
    );
  }

  try {
    const pkgDir = path.dirname(require.resolve(`${pkg}/package.json`));
    const ext = process.platform === "win32" ? ".exe" : "";
    return path.join(pkgDir, "bin", `winload${ext}`);
  } catch {
    throw new Error(
      `winload: platform package "${pkg}" not found\n` +
      `Try reinstalling one of:\n` +
      `  npm install @vincentzyuapps/winload\n` +
      `  npm install winload-rust-bin\n` +
      `  npm install @vincentzyuapps/winload --registry https://npm.pkg.github.com\n` +
      `Or download manually: https://github.com/VincentZyuApps/winload/releases`
    );
  }
}

module.exports = { getBinaryPath, PLATFORMS };
