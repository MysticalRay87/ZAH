from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame
from PyQt6.QtCore import Qt

class MainCockpit(QMainWindow):
    """
    Screen 3: Main Administration Cockpit Dashboard.
    The primary hub for server telemetry and command execution.
    """
    def __init__(self):
        super().__init__()

        # --- Dashboard Configuration ---
        self.setWindowTitle("Zero-G Admin Helper - Main Cockpit")
        self.setFixedSize(1000, 750)
        
        # --- Central UI Canvas ---
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # --- Grid Layout Definition ---
        self.layout = QGridLayout(self.central_widget)
        self.central_widget.setContentsMargins( 10, 10, 10, 10)
        self.central_widget.setSpacing(10)

        # Zone Definition (Conceptual placeholders)
        # Zone A: Telemetry Panel (Top Left)
        # Zone B: Command Console (Bottom Span)
        self.setup_zones()
        
        # Initial log confirmation for registry sync
        print("[SUCCESS] Main Cockpit Dashboard initialized.")

    def setup_zones(self):
        # Create a frame for the console (Zone B)
        self.console_frame = QFrame()
        self.console_frame.setObjectName("ConsoleFrame")
        self.grid.addWidget(self.console_frame, 2, 0, 1, 3) # Row 2, Col 0, 1 row height, 3 cols wide
        
        print("[SUCCESS] Main Cockpit grid initialized.")