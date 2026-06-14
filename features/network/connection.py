import os
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class NetworkWizardOverlay(QWidget):
    def __init__(self):
        super().__init__()
        
        # Enforce strict 512x512 square viewport bounds
        self.win_size = 512
        
        self.setWindowTitle("Zero-G Admin Helper - Network Wizard")
        self.setFixedSize(self.win_size, self.win_size)
        
        # Initialize background canvas container
        self.bg_canvas = QLabel(self)
        self.bg_canvas.setGeometry(0, 0, self.win_size, self.win_size)
        self.bg_canvas.setScaledContents(True)
        
        # Discover project folder directory root path dynamically
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
        
        # Resolve target graphic asset location
        img_path = os.path.join(project_root, "assets", "backgrounds", "network_connection_wizard.png")
        
        if os.path.exists(img_path):
            self.bg_canvas.setPixmap(QPixmap(img_path))
            print("[INFO] Screen 1: Network Connection Wizard layout rendered successfully.")
        else:
            print(f"[ERROR] Asset path lookup failure at: {img_path}")
            self.bg_canvas.setText("Missing background image asset.")
            self.bg_canvas.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.bg_canvas.setStyleSheet("color: #00ffff; background-color: #0c1020; font-size: 14px;")

        # FIXED QSS: Explicitly forcing placeholder text layers to render visibly
        field_qss = """
            QLineEdit {
                border: none;
                background: transparent;
                color: #00ffff;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 14px;
                padding-left: 5px;
            }
            QLineEdit::placeholder {
                color: rgba(0, 255, 255, 100); /* Semi-transparent cyan placeholder */
            }
        """
        
        # Exact input coordinates matching your placement adjustments
        self.input_ip = QLineEdit(self)
        self.input_ip.setGeometry(120, 170, 320, 30)
        self.input_ip.setStyleSheet(field_qss)
        self.input_ip.setPlaceholderText("IP Address")
        
        self.input_port = QLineEdit(self)
        self.input_port.setGeometry(120, 247, 320, 30)
        self.input_port.setStyleSheet(field_qss)
        self.input_port.setPlaceholderText("TelNET Port")
        
        self.input_pass = QLineEdit(self)
        self.input_pass.setGeometry(120, 325, 320, 30)
        self.input_pass.setStyleSheet(field_qss)
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_pass.setPlaceholderText("Enter Auth Token (Password)")

        # Completely transparent button styling parameters
        btn_qss = "QPushButton { border: none; background: transparent; }"
        
        # Accept Button (Processes input variables)
        self.btn_accept = QPushButton(self)
        self.btn_accept.setGeometry(65, 400, 135, 35)
        self.btn_accept.setStyleSheet(btn_qss)
        self.btn_accept.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_accept.clicked.connect(self.accept_action_callback)
        
        self.btn_accept.setDefault(True)
     
        # Cancel Button (Safely terminates process loop)
        self.btn_cancel = QPushButton(self)
        self.btn_cancel.setGeometry(220, 400, 135, 35)
        self.btn_cancel.setStyleSheet(btn_qss)
        self.btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_cancel.clicked.connect(self.cancel_action_callback)

        # Reset Button (Clears user inputs and restores placeholder visibility)
        self.btn_reset = QPushButton(self)
        self.btn_reset.setGeometry(380, 400, 70, 35)
        self.btn_reset.setStyleSheet(btn_qss)
        self.btn_reset.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_reset.clicked.connect(self.reset_action_callback)   
       
    def secure_password_typing_callback(self, text_value):
        """Dynamic slot that applies password dots only when text characters are present."""
        if text_value:
            self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            self.input_pass.setEchoMode(QLineEdit.EchoMode.Normal)

    def reset_action_callback(self):
        print("[UI EVENT] Clear input fields executed. Restoring placeholder strings.")

        # Clear text strings completely out of system memory
        self.input_ip.clear()
        self.input_port.clear()

        # Safe password reset sequence: Isolate listener signals during visibility flip
        self.input_pass.blockSignals(True)
        self.input_pass.clear()
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Normal)
        self.input_pass.blockSignals(False)

        # Force individual widget components to flush visual buffers immediately
        self.input_ip.update()
        self.input_port.update()
        self.input_pass.update()
        self.update()

    def cancel_action_callback(self):
        print("[UI EVENT] Cancel clicked. Shutting down application loop cleanly...")
        self.close()

    def accept_action_callback(self):
        print("\n==================================================")
        print("PRODUCTION WIZARD DATA INGESTION (512x512)")
        print("==================================================")
        print(f"IP Target     : {self.input_ip.text() if self.input_ip.text() else 'BLANK'}")
        print(f"Port Target   : {self.input_port.text() if self.input_port.text() else 'BLANK'}")
        print("==================================================")