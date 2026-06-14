import os
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QTimer, Qt, QRectF, QCoreApplication
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QFont, QPainterPath

try:
    from features.auth.login import LoginWindow
except ImportError:
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    from features.auth.login import LoginWindow

class ApplicationLoader(QDialog):
    """Screen 1A: Zero-G Advanced Loader - Active Event Pumping Engine"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        print("[DEBUG] Initializing safe loader with active event loop pumping...")

        self.setFixedSize(1000, 750)
        self.setWindowTitle("System Initialization")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "../../"))
        
        bg_path = os.path.join(project_root, "assets/backgrounds/loading_screen.png")
        logo_path = os.path.join(project_root, "assets/branding/ZAH_emblem.png")

        self.bg_pixmap = QPixmap(os.path.normpath(bg_path))
        self.logo_pixmap = QPixmap(os.path.normpath(logo_path))

        self.current_progress = 0       
        self.pulse_offset = 0.0         
        
        self.account_checkpoint_cleared = False
        self.network_checkpoint_cleared = False

        self.boot_timer = QTimer(self)
        self.boot_timer.timeout.connect(self.advance_loading_cycle)
        self.initialize_circuit_paths()

    def initialize_circuit_paths(self):
        self.circuit_paths = []
        
        p1 = QPainterPath()
        p1.moveTo(50, 350); p1.lineTo(200, 350); p1.lineTo(280, 280); p1.lineTo(350, 280)
        self.circuit_paths.append(p1)

        p2 = QPainterPath()
        p2.moveTo(950, 350); p2.lineTo(800, 350); p2.lineTo(720, 420); p2.lineTo(650, 420)
        self.circuit_paths.append(p2)

        p3 = QPainterPath()
        p3.moveTo(500, 50); p3.lineTo(500, 150); p3.lineTo(450, 200)
        self.circuit_paths.append(p3)

        p4 = QPainterPath()
        p4.moveTo(500, 700); p4.lineTo(500, 600); p4.lineTo(550, 550)
        self.circuit_paths.append(p4)

    def start_boot_sequence(self):
        print("[STATUS] Starting timeline synchronization loop...")
        self.boot_timer.start(30)

    def advance_loading_cycle(self):
        # Always update line animation coordinates
        self.pulse_offset += 5.0
        if self.pulse_offset >= 200.0:
            self.pulse_offset = 0.0

        # --- MILESTONE INTERCEPT 1: LOGIN POPUP WITH PUMPED ANIMATIONS ---
        if self.current_progress == 30 and not self.account_checkpoint_cleared:
            print("[CHECKPOINT] 30% Milestone Hit. Launching login challenge...")
            
            # Spin up the login dialog
            login_popup = LoginWindow(self)
            
            # Make the login popup visible asynchronously so we don't starve the thread
            login_popup.show()
            
            # Run a manual pumping loop right here while the popup window remains visible!
            while login_popup.isVisible():
                # 1. Update the line dash positions so they keep traveling
                self.pulse_offset += 0.15 # Fine-tuned step size during dialogue pause
                if self.pulse_offset >= 200.0:
                    self.pulse_offset = 0.0
                    
                # 2. Force the loader window to redraw its neon canvas lines
                self.update()
                
                # 3. Pump the system event queues to keep inputs and visuals completely awake
                QCoreApplication.processEvents()
                
            # Evaluate the return code once the loop terminates (via Accept or Cancel/X)
            if login_popup.result() == QDialog.DialogCode.Accepted:
                print("[SUCCESS] Credentials cleared. Unlocking timeline updates...")
                self.account_checkpoint_cleared = True
            else:
                print("[TERMINATION] Login process dismissed or aborted. Shutting down...")
                self.boot_timer.stop()
                self.reject()
                return

        # --- MILESTONE INTERCEPT 2: 60% NETWORK CONFIGURATION GATE ---
        if self.current_progress == 60 and not self.network_checkpoint_cleared:
            print("[CHECKPOINT] 60% Milestone Hit. Processing network configuration rules...")
            self.network_checkpoint_cleared = True

        # Increment layout progress bars
        self.current_progress += 1
        self.update()

        if self.current_progress >= 100:
            self.boot_timer.stop()
            print("[SUCCESS] Pipeline clear. Launching workspace dashboard...")
            self.accept()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if not self.bg_pixmap.isNull():
            painter.drawPixmap(0, 0, 1000, 750, self.bg_pixmap)

        underlay_pen = QPen(QColor("#11293a"), 1.5, Qt.PenStyle.SolidLine)
        painter.setPen(underlay_pen)
        for path in self.circuit_paths:
            painter.drawPath(path)

        pulse_glow_pen = QPen(QColor(0, 255, 255, 40), 5.0)  
        pulse_glow_pen.setDashPattern([30, 150]); pulse_glow_pen.setDashOffset(self.pulse_offset)
        pulse_core_pen = QPen(QColor("#00ffff"), 1.8)        
        pulse_core_pen.setDashPattern([30, 150]); pulse_core_pen.setDashOffset(self.pulse_offset)

        painter.setPen(pulse_glow_pen)
        for path in self.circuit_paths:
            painter.drawPath(path)

        painter.setPen(pulse_core_pen)
        for path in self.circuit_paths:
            painter.drawPath(path)

        if not self.logo_pixmap.isNull():
            painter.save()
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
            
            target_height = 420.0  
            scale_factor = target_height / self.logo_pixmap.height()
            target_width = self.logo_pixmap.width() * scale_factor
            target_x = (1000.0 - target_width) / 2.5
            target_y = 190
            
            logo_rect = QRectF(target_x, target_y, target_width, target_height)
            painter.drawPixmap(logo_rect, self.logo_pixmap, QRectF(self.logo_pixmap.rect()))
            painter.restore()

        text_rect = QRectF(100, 620, 800, 40)
        painter.setPen(QColor("#00ffff"))
        font = QFont("Courier New", 14, QFont.Weight.Bold)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 2)
        painter.setFont(font)
        
        status_msg = f"INITIALIZING SYSTEM ARCHITECTURE... {self.current_progress}%" if self.current_progress < 100 else "ALL MODULES ONLINE"
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, status_msg)