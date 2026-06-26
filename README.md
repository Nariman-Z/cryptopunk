<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<!-- Dynamic Header -->
<img height=350 alt="Repo Banner - cryptopunk" src="https://capsule-render.vercel.app/api?type=waving&color=0:6E9EAB,100:23395B&height=300&section=header&text=🔮cryptopunk&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Interactive%20Curses%20OpenSSL%20Password%20Generation%20Engine&descAlignY=60&descAlign=50"></img>

<!--Title-->
<p align="center">
  <b>📟 Terminal-Native High-Entropy Keygen Ecosystem (v1.0.0)</b>
  <br> <small> <i>- A sleek, terminal-optimized cryptographic utility featuring real-time entropy evaluations, contextual control layouts, and cross-platform binary distribution -</i> </small> <br>
</p> 

---

## 🔧 Introduction

Project cryptopunk is a high-performance, terminal-native **password generation environment** engineered with Python and the `curses` framework. It provides a lightning-fast, secure UI that runs entirely inside your shell, bypassing browser-based generators or unencrypted tools. Features include:

* **Entropy Estimation Pipeline:** High-fidelity, real-time bit strength analytics using standard information-theory constraints.
* **Context-Aware Architecture:** Dynamic control layouts that automatically swap key bindings (e.g., matching instant generation vs. custom regeneration states).
* **Hardened Cryptography Backhaul:** Relies natively on standard OS random-number pools and provides precise OpenSSL structural export definitions.
* **Clipboard Management Integrations:** Low-latency shell subprocess pipelines to hook seamlessly into Linux and Windows system clipboards.

Ideally suited for system administrators, security engineers, and enthusiasts who live inside standard terminal configurations.

---

## ⚙️ Software Dependencies

| Component / Tool | Functional Overview |
| --- | --- |
| **Python 3.12+** | Core execution runtime driving asynchronous state logic and calculations. |
| **Curses Engine** | High-efficiency terminal manipulation wrapper providing raw key events and cell rendering. |
| **xclip / xsel** | Optional Linux dependencies used to bridge password variables seamlessly to the X11 clipboard environment. |
| **PyInstaller** | Binary deployment framework used to cook multi-platform standalone click-to-run assets. |

---

## 💻 System Architecture

Implemented via a modular **Python 3 Standard Library** structure utilizing safe, decoupled functional paradigms:

### Core Execution Modules

* **Secrets-Driven Entropy Engine** Utilizes the cryptographically secure `secrets` resource pool rather than standard pseudo-random packages to safeguard against algorithmic prediction.
* **Dynamic Math Estimation Layout** Computes real-time pool sizes and applies logarithmic scale calculation rules ($E = \log_2(L^{P})$) to display precise bits of entropy dynamically.
* **Asynchronous Key-Event Loop** A single non-blocking listening loop filtering low-level curses hex keycaps into dynamic option toggles and UI redraws.
* **State Array Sanitizers** Internal string mapping modules that dynamically sanitize pool options when similar (`l1I0O`) or ambiguous configurations are active.

### Automation & Deployment Pipeline

* **Cross-Platform Compilation Factories** GitHub Actions runners that spins up native Windows and Linux containers to map project code into executable standalone packages.
* **Semantic Tag Control** Automated release-trigger mechanisms filtering configuration snapshots straight into proper versioning buckets.
* **Silent Subprocess Isolation** Spawns asynchronous browser utilities using `stdout/stderr` redirection barriers to prevent debug warnings from cluttering terminal cell positioning.

---

## 🚀 Release & Distribution

`cryptopunk` ships with a fully automated cross-platform release pipeline powered by GitHub Actions.

### Build Pipeline Features

* ✅ Automated Linux and Windows executable generation
* ✅ Versioned GitHub Releases with attached binaries
* ✅ Windows-specific `windows-curses` dependency injection
* ✅ Console flag optimizations for native Windows terminal support
* ✅ Artifact packaging and release publishing
* ✅ Permission-aware workflow configuration for seamless updates

The release workflow ensures every tagged version is automatically compiled and distributed without requiring local build tooling.

---

## 🌐 Quick Guide Interface Topography

| Input Shortcut | Visual Icon | Operational Scope | System Response |
| --- | --- | --- | --- |
| **UP / DOWN** | `↑↓` | Navigation through parameters list | Changes option selection focus |
| **LEFT / RIGHT** | `←→` | Alter active password width constraints | Shrinks or grows targeted scale (4 - 64) |
| **SPACE** | `Space` | Option checkbox toggling | Live-swaps character criteria status |
| **R / G** | `[R]` | Instantaneous password recreation | Refreshes text array and recalculates entropy |
| **C** | `[C]` | Clipboard transport sequence | Pipes pure output to main OS copy deck |
| **S** | `[S]` | Backup pipeline trigger | Saves current state data locally |
| **E** | `[E]` | Terminal export command generator | Copies matching OpenSSL shell execution string |
| **I** | `[I]` | Version lookup & community documentation | Launches upstream project repo safely in browser |
| **Q / ESC** | `[Q]` | UI destruction routine | Restores standard terminal cells and exits |

---

## 🛡️ Reliability Improvements

Recent updates focused on making `cryptopunk` more resilient across different terminal environments:

* **Dynamic Terminal Resize Handling** – The application no longer exits when the terminal becomes too small. Instead, it gracefully waits until sufficient space is available again.
* **Improved Screen Restoration** – Better handling of unexpected terminal states and redraw operations.
* **Enhanced Cross-Platform Compatibility** – Additional safeguards for Linux and Windows console implementations.

---

## 📜 Version Ledger

| Version    | Release Date | Highlights                                                                                                                                |
| ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **v1.0.2** | June 2026    | Added write permissions to release workflows and improved automated artifact publishing reliability.                                      |
| **v1.0.3** | June 2026    | Introduced Windows-specific build improvements, console flag optimizations, and automatic `windows-curses` dependency injection.          |
| **v1.0.4** | June 2026    | Production optimizations and release pipeline refinements for more stable cross-platform binary distribution.                             |
| **v1.0.5** | June 2026    | Improved terminal resilience by gracefully handling terminal resize events and preventing application exits on small terminal dimensions. |

---

## 🦾 Contributing & Dev Cycle
Want to hack on `cryptopunk`? Contributions, feature requests, and bug reports are welcome! Whether you are fixing a UI grid misalignment, optimizing the entropy math, or adding platform support, here is how to get involved:

### Development Workflow

1. **Fork the Repository** — Create a personal copy of the project deck.
2. **Create a Feature Branch** — Keep your changes isolated (`git checkout -b feature/amazing-tweak`).
3. **Commit with Theme Emojis** — Use clean messages with terminal styling context (e.g., `update: expand option views`).
4. **Open a Pull Request** — Submit your branch against `main` with a clear summary of your structural modifications.

Found a bug or have an idea? Skip the code and open an interactive issue ticket on the tracker directly!

### Ways to Contribute

* 🐛 Bug fixes
* ✨ New features
* 🎨 UI/UX improvements
* 📚 Documentation improvements
* 🧪 Testing on additional platforms
* 🔒 Security reviews

Every contribution, no matter how small, helps make `cryptopunk` better.

---

## 📚 License

Licensed under the terms of the **MIT License**. This project is completely open and free for both personal and commercial use—just keep the original copyright notice intact. For full details, see the companion [LICENSE](https://github.com/Nariman-Z/cryptopunk/blob/main/LICENSE) file.

---

<div align="center">

## Made with vibe & caffeine ☕
[![Maintainer](https://img.shields.io/badge/Built%20and%20maintained%20by:-Nariman%20Ziaie-C0392B?style=plastic)](https://github.com/Nariman-Z)

Contributors:

[![Contributor #1](https://img.shields.io/badge/%231-Omid--H-2980B9?style=plastic)](https://github.com/Omid-H)

</div>

<!-- Gradient Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


*Last Updated: June 26, 2026*
