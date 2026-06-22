from PyQt6.QtCore import QThread, pyqtSignal
import time

class TelemetryWorker(QThread):
    """Worker thread for background network/log monitoring."""
    
    # Signal emitted when a new log line is received
    log_received = pyqtSignal(str)
    connection_status = pyqtSignal(bool)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.running = True

    def run(self):
        print(f"[THREAD] Telemetry worker started on {self.host}:{self.port}")
        # Simulate initial connection status
        self.connection_status.emit(True)
        
        while self.running:
            # Placeholder for actual socket read logic
            # In production, this will parse the raw Telnet stream
            time.sleep(1) # Network polling interval
            self.log_received.emit(f"Telemetry sync at {time.time()}")
            
    def stop(self):
        self.running = False
        self.wait()