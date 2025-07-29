from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt


class Ui_MainWindow:
    def __init__(self, MainWindow):
        self.setup_ui(MainWindow)

    def setup_ui(self, MainWindow):
        MainWindow.setWindowTitle("Media Trimmer Tool")
        MainWindow.setGeometry(100, 100, 800, 600)

        # Create widgets
        self.video_frame = QWidget(MainWindow)
        self.play_pause_button = QPushButton("Play/Pause", MainWindow) 
        self.load_button = QPushButton("Load Video", MainWindow)
        self.status_label = QLabel("Status: Ready", MainWindow)
        
        # Time labels
        self.current_time_label = QLabel("Current Time: 00:00", MainWindow)
        self.total_time_label = QLabel("Total Time: 00:00", MainWindow)
        

        # Layout for control buttons
        controls = QHBoxLayout()
        controls.addWidget(self.play_pause_button)
        controls.addWidget(self.load_button)
   

        # Layout for time labels
        time_layout = QHBoxLayout()
        time_layout.addWidget(self.current_time_label)
        time_layout.addWidget(self.total_time_label)

        # Main layout
        layout = QVBoxLayout()
 
        layout.addWidget(self.video_frame)
        layout.addLayout(controls)
        layout.addLayout(time_layout)
        layout.addWidget(self.status_label)

        central_widget = QWidget(MainWindow)
        central_widget.setLayout(layout)
        MainWindow.setCentralWidget(central_widget)
