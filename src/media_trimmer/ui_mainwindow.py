from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QSlider, QHBoxLayout
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
        self.current_time_label = QLabel("Current Time: 0:00:00:00", MainWindow)
        self.total_time_label = QLabel("Total Time:  0:00:00:00", MainWindow)



        # Layout for control buttons
        controls = QHBoxLayout()
        controls.addWidget(self.play_pause_button)
        controls.addWidget(self.load_button)
        
        
        # Time Jump Layout
        jump_layout = QHBoxLayout()
        jump_layout.setSpacing(0)  # Remove spacing between widgets
        jump_layout.setContentsMargins(0, 0, 0, 0)  # Optional: Remove outer margins
        jump_title=QLabel("Jump to:")
        jump_title.setFixedWidth(50)
        jump_layout.addWidget(jump_title)

        # Hour Input
        self.hour_input = QLineEdit()
        self.hour_input.setFixedWidth(30)
        self.hour_input.setPlaceholderText("HH")  # <-- Placeholder
        jump_layout.addWidget(self.hour_input)

        # Colon Separator :
        colon1 = QLabel(":")
        colon1.setFixedWidth(5)
        jump_layout.addWidget(colon1)

        # Minute Input
        self.minute_input = QLineEdit()
        self.minute_input.setFixedWidth(30)
        self.minute_input.setPlaceholderText("MM")  # <-- Placeholder
        jump_layout.addWidget(self.minute_input)

        # Colon Separator :
        colon2 = QLabel(":")
        colon2.setFixedWidth(5)
        jump_layout.addWidget(colon2)

        # Second Input
        self.second_input = QLineEdit()
        self.second_input.setFixedWidth(30)
        self.second_input.setPlaceholderText("SS")  # <-- Placeholder
        jump_layout.addWidget(self.second_input)

        # Dot Separator .
        dot = QLabel(".")
        dot.setFixedWidth(5)
        jump_layout.addWidget(dot)

        # Millisecond Input
        self.millisecond_input = QLineEdit()
        self.millisecond_input.setFixedWidth(30)
        self.millisecond_input.setPlaceholderText("MS")  # <-- Placeholder
        jump_layout.addWidget(self.millisecond_input)


        # Jump Button
        self.jump_button = QPushButton("Jump")
        self.jump_button.setFixedWidth(50)
        jump_layout.addWidget(self.jump_button)
        jump_layout.addStretch(1)


        # Layout for time labels
        time_layout = QHBoxLayout()
        time_layout.addWidget(self.current_time_label)
        time_layout.addWidget(self.total_time_label)

        # Main layout
        layout = QVBoxLayout()
 
        layout.addWidget(self.video_frame)
        layout.addLayout(controls)
        layout.addLayout(time_layout)
        layout.addLayout(jump_layout)
        layout.addWidget(self.status_label)

        central_widget = QWidget(MainWindow)
        central_widget.setLayout(layout)
        MainWindow.setCentralWidget(central_widget)
