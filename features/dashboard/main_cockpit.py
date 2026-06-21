from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
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
        self.layout = QVBoxLayout(self.central_widget)
        
        # Initial log confirmation for registry sync
        print("[SUCCESS] Main Cockpit Dashboard initialized.")