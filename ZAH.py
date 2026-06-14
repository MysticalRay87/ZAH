import os
import sys
from PyQt6.QtWidgets import QApplication

# -------------------------------------------------------------------
# MULTI-TIER PACKAGE NAMESPACE RESOLUTION
# -------------------------------------------------------------------

# Load Screen 1 (The Application Loader Component)
try:
    from features.loading.loading_screen import ApplicationLoader
    print("[SUCCESS] Package Namespace: ApplicationLoader Loaded")
except ImportError as e:
    print(f"[WARNING] Could not load Application Loader: {e}")
    ApplicationLoader = None

# Load Screen 2 (The Onboarding Wizard)
try:
    from features.auth.onboarding import AccountOnboardingWizard
    print("[SUCCESS] Package Namespace: AccountOnboardingWizard Loaded")
except ImportError as e:
    print(f"[WARNING] Could not load Onboarding Wizard: {e}")
    AccountOnboardingWizard = None

def main():
    print("[DEBUG] Initializing Master Operational Registry Engine (PyQt6 Mode)...")

    # Initialize the core global window event loop using PyQt6
    app = QApplication(sys.argv)

    # Dynamic Project Root Asset Traversal for the CSS Stylesheet
    root_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(root_dir, "assets/ZAH.css")

    # Ingest the centralized stylesheet via an immutable read stream
    if os.path.exists(css_path):
        try:
            with open(css_path, "r", encoding="utf-8") as stream:
                css_rules = stream.read()
                app.setStyleSheet(css_rules)
            print("[SUCCESS] Central layout stylesheet applied: ZAH.css, Cyan-Theme")
        except Exception as e:
            print(f"[ERROR] Failed to read central stylesheet: {e}")
    else:
        print(f"[WARNING] Local asset missing at: {css_path}. Using default system styles.")

    # -------------------------------------------------------------------
    # SEQUENTIAL BOOT LIFECYCLE MANAGEMENT LOOP
    # -------------------------------------------------------------------
    
    # PHASE 1: Deploy Screen 1 (The Non-Blocking Animated Loader)
    if ApplicationLoader is not None:
        print("[DEBUG] Instantiating Screen 1: Application Splash Loader Canvas...")
        loader = ApplicationLoader()
        
        # Public method call to kick off the internal QTimer countdown
        loader.start_boot_sequence()
        
        # Freeze main thread here; wait for loader to hit 100% and call accept()
        loader_exit_code = loader.exec()
        
        # If the user closed the loader window prematurely, abort the entire stack
        if loader_exit_code == 0:
            print("[STATUS] Loading phase interrupted by operator. Aborting execution loop.")
            sys.exit(0)
    else:
        print("[ERROR] Critical Component Failure: ApplicationLoader is missing. Aborting.")
        sys.exit(1)

    # PHASE 2: Deploy Screen 2 (The Unified Account Creation Wizard)
    if AccountOnboardingWizard is not None:
        print("[DEBUG] Instantiating Screen 2: Account Onboarding Wizard Canvas...")
        wizard = AccountOnboardingWizard()
        
        # Freeze main thread here; wait for form to validate and call accept()
        wizard_exit_code = wizard.exec()
        
        # Evaluate how the user exited Screen 2
        if wizard_exit_code == 1:
            print("[SUCCESS] Onboarding profile verified. Handoff to core environment complete.")
        else:
            print("[STATUS] Wizard deployment canceled by operator. Cleaning up local variables.")
            sys.exit(0)
    else:
        print("[ERROR] Critical Component Failure: AccountOnboardingWizard is missing. Aborting.")
        sys.exit(1)

    # FUTURE PHASE 3: Launch Primary System Administration Dashboard Frame
    print("[STATUS] All initialization gates clear. Spinning up master core cockpit dashboard view...")
    # This is where your main workspace screen will show up later!

if __name__ == "__main__":
    main()