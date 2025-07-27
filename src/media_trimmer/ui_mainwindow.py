# PyQt5 UI layout code
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QSlider, QHBoxLayout

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Trimmer Tool")
        self.setGeometry(100, 100, 800, 600)

        self.video_frame = QWidget(self)
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.load_button = QPushButton("Load Video")
        self.trim_button = QPushButton("Trim Selection")
        self.status_label = QLabel("Status: Ready")
        
        self.slider = QSlider()
        self.slider.setOrientation(1)  # Horizontal slider

        # Layout
        controls = QHBoxLayout()
        controls.addWidget(self.load_button)
        controls.addWidget(self.play_button)
        controls.addWidget(self.pause_button)
        controls.addWidget(self.trim_button)

        layout = QVBoxLayout()
        layout.addWidget(self.video_frame)
        layout.addWidget(self.slider)
        layout.addLayout(controls)
        layout.addWidget(self.status_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
