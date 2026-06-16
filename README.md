# Zero-G Admin Helper (v1.0-Alpha)

An immersive, terminal-integrated desktop administration station designed for managing an Empyrion: Galactic Survival dedicated server. This application drops traditional corporate design conventions in favor of a high-tech, dark-themed sci-fi cockpit HUD utilizing PySide6/PyQt6 and asynchronous background streaming threads.

---

## 🏗️ Core Architecture & Patterns

This repository strictly enforces the following architectural parameters via its Notebook Master Operational Registry:

1. **Feature-First Pattern:** All functional business logic, controllers, and sub-views are completely encapsulated within their own isolated sub-directories under `/features/`. Cross-module dependency is strictly prohibited.
2. **State Separation Protocol:** Dynamic runtime data, state caches, persistent configurations, and console logs are housed inside the root `/data/` directory and hard-blocked from Git version tracking via `.gitignore`.
3. **Fixed Entry Points:** System discovery relies on root-anchored paths. `ZAH.py` serves as the primary orchestration launcher, and `startup.py` manages initial system diagnostics.

---

## 📦 Isolated Module Registry (`/features/`)

* **`loading/`** - Orchestrates initial sequence verification, system diagnostics, and credential routing flows.
* **`auth/`** - Manages account setup validation and interactive user login wizards.
* **`network/`** - Controls asynchronous TelNET connection initializations and input stream handshakes.
* **`dashboard/`** - Renders the main cockpit telemetry display interface, handling background-threaded log buffers and live game chat processing.

---

## 🚀 Terminal Execution Hook
To securely initialize interactive development sessions with local safety backups, execute the custom macro command:
```bash
gemini-gocat << 'EOF' > /mnt/Zero-G_Files/Zero-G_Admin_Helper/README.md
# Zero-G Admin Helper (v5.1.0-Alpha)

An immersive, high-tech sci-fi standalone desktop administration station designed to monitor a dedicated Empyrion Galactic Survival game server environment and handle live, in-game administration operations. 

---

## 🏗️ Technical Stack & Framework Constraints

* **Framework:** PyQt6 (Strict usage of scoped enum namespaces like `Qt.AlignmentFlag` and `Qt.Orientation`).
* **Root Workspace Path:** `/mnt/Zero-G_Files/Zero-G_Admin_Helper`
* **Line Terminations:** All outbound server commands must use `\r\n` line terminations paired with a 500ms input buffer delay to match GTX Gaming hardware calibrations.

---

## 🌌 Aesthetic Identity & UI Guidelines

The interface moves completely away from traditional flat, corporate grey layouts to model an immersive starship cockpit HUD utilizing custom widget textures:
* **Deep Space Backgrounds:** Shadowy Marine Blue (`#001A33` / RGB: 0, 26, 51).
* **Neon Accent Tones:** Bright Cerulean Blue (`#1DACD6` / RGB: 29, 172, 214) and Vivid Cerulean (`#007BA7` / RGB: 0, 123, 167).
* **UI Integrity:** Strict reliance on QSS `border-image` styling to ensure highly detailed vector corner brackets and neon glow effects stay crisp and perfectly unwarped across all monitor resolutions.

---

## 📦 System Architecture & Directory Patterns

This repository enforces strict **Feature-First Pattern** boundaries and **State Separation Protocols**. All code tracking is restricted by these root namespaces:

* `assets/` - Immersive cockpit UI themes, buttons, backgrounds, and branding elements.
* `components/` - Reusable custom UI components.
* `data/` - Persistent configuration, server JSON tables, and caches (Excluded from Git tracking).
* `logs/` - Outbound stdout console streams and local debug traces (Excluded from Git tracking).
* `theme/` - Dynamic QSS stylesheets (`cyan_theme.qss`) and color palette controllers.
* `main_window/` - Central structural base framework for the core administration layout.
* `services/` - Background networking utilities, server threads, and credential managers.
* `features/` - Strictly isolated functional views and sub-module business logic:
  - `startup/` - Discovery paths and initial file verification loops.
  - `admin_deck/` - Core console interfaces.
  - `data_feed/` - Layout panels and telemetry dropdown choices.
  - `monitoring/` - CPU/RAM host node utilization arrays.
  - `player_management/` - In-game user profile and inventory cards.
  - `server_manager/` - Hardware controls and server scripts.

---

## 🔄 Automated Lifecycle & Sequential Flows

### 1. Boot Diagnostics & Loading Screen Logic
The application initialization sequence uses sequential milestones to analyze local files before launching core windows:
* **30% Milestone (User Login Check):** Scans for local user session logs. If absent, shifts to the `Login Screen` or cascades directly into the `Account Creation Wizard` (Requires 6-character username, 8-character alphanumeric matching password, and Primary/Secondary account type designation).
* **60% Milestone (Network Connection Check):** Scans for host system parameters (IP Address, Telnet Port, and Token/Password). If first-time login or configuration files are missing, intercepts execution to load the `Network Connection Wizard` (Features custom inputs and input reset utility loops).

### 2. Workspace Automations
* **Automated Safety Commit:** Executed via `gemini-go` inside the terminal to back up the current workspace prior to AI agent execution.
* **Automated Cleanups:** Automated Git snapshot generation with customized vertical CHANGELOG tracking, paired with systematic `__pycache__` bytecode directory vaporization upon program closure.

---

## 📡 Remote Server Connection Variables
* **Target Host:** Dedicated Empyrion Server hosted via GTX Gaming
* **Active Destination IP:** `66.23.236.138`
* **Active Routing Port:** `30004` (Dedicated text-based Telnet console log stream)
* **Authentication Token:** `535ue`
