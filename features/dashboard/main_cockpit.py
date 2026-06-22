from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout, QTextEdit
from PyQt6.QtCore import Qt

from features.dashboard.telemetry_worker import TelemetryWorker

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
        self.grid = QGridLayout(self.central_widget)
        self.grid.setContentsMargins( 10, 10, 10, 10)
        self.grid.setSpacing(10)

        # --------------------------------------------------
        # Zone Definition
        # --------------------------------------------------

        # Zone A: Telemetry Panel (Top Left)
        self.telemetry_panel = TelemetryPanel("SYSTEM LOAD")
        self.telemetry_panel.setObjectName("TelemetryPanel")
        self.grid.addWidget(self.telemetry_panel, 0, 0, 1, 1)

        # Zone B: Console Output (Full Bottom Span)
        self.console_frame = QFrame()
        self.console_frame.setObjectName("ConsoleFrame")
        self.console_layout = QVBoxLayout(self.console_frame)
        
        # Console output widget
        self.console = QTextEdit()
        self.console.setObjectName("ConsoleDisplay")
        self.console.setReadOnly(True)
        self.console_layout.addWidget(self.console)
        
        # Span across 3 columns at Row 2
        self.grid.addWidget(self.console_frame, 2, 0, 1, 3)
        
        # --- Telemetry Engine Initialization ---
        self.telemetry_worker = TelemetryWorker("127.0.0.1", 30004)
        self.telemetry_worker.log_received.connect(self.update_console_output)
        self.telemetry_worker.start()
        
        # Initial log confirmation for registry sync
        print("[SUCCESS] Main Cockpit Dashboard initialized.")

    def setup_zones(self):
        # Create a frame for the console (Zone B)
        self.console_frame = QFrame()
        self.console_frame.setObjectName("ConsoleFrame")
        self.console_layout = QVBoxLayout(self.console_frame)
        
        # Integrated Console Output
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console_layout.addWidget(self.console)
        
        self.grid.addWidget(self.console_frame, 2, 0, 1, 3) # Row 2, Col 0, 1 row height, 3 cols wide
        
        # New Telemetry Panel
        self.telemetry_panel = TelemetryPanel("SYSTEM LOAD")
        self.grid.addWidget(self.telemetry_panel, 0, 0, 1, 1) # Positioned top-left

        print("[SUCCESS] Main Cockpit grid initialized.")

    def update_console_output(self, log_line):
        """Slot to receive signal from worker and update UI."""
        self.console.append(log_line)

    def closeEvent(self, event):
        """Ensure thread stops when window closes."""
        self.telemetry_worker.stop()
        event.accept()


class TelemetryPanel(QFrame):
    def __init__(self, title):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        self.layout = QVBoxLayout(self)
        
        # Panel Title
        self.title_label = QLabel(title)
        self.layout.addWidget(self.title_label)
        
        # Telemetry Data Placeholder
        self.data_label = QLabel("INITIALIZING...")
        self.layout.addWidget(self.data_label)