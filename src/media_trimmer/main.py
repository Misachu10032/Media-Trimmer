import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from media_trimmer.ui_mainwindow import Ui_MainWindow
from media_trimmer.player_widget import VLCPlayer
from media_trimmer.trimmer import trim_video

class MediaTrimmerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI (controls and labels)
        self.ui = Ui_MainWindow(self)
        
        # Initialize VLCPlayer with UI components
        self.player = VLCPlayer(self.ui.video_frame, self.ui.slider, self.ui.status_label)
        
        # Connect the VLCPlayer signal for time updates to the method that updates the labels
        self.player.time_update_signal.connect(self.update_time_labels)
        
        # Connect buttons to player functions
        self.ui.load_button.clicked.connect(self.load_video)
        self.ui.play_button.clicked.connect(self.player.play)
        self.ui.pause_button.clicked.connect(self.player.pause)

    def load_video(self):
        # Open file dialog to load a video file
        filename, _ = QFileDialog.getOpenFileName(self, "Select Video")
        if filename:
            self.ui.status_label.setText(f"Loaded: {filename}")
            self.player.set_media(filename)

    def update_time_labels(self, current_time, total_time):
        """Update the time labels with the current and total time."""
        current_time_str = self.format_time(current_time)
        total_time_str = self.format_time(total_time)
        
        self.ui.current_time_label.setText(f"Current Time: {current_time_str}")
        self.ui.total_time_label.setText(f"Total Time: {total_time_str}")

    def format_time(self, time_in_ms):
        """Convert time in milliseconds to mm:ss format."""
        seconds = time_in_ms // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{int(minutes):02}:{int(seconds):02}"


def main():
    app = QApplication(sys.argv)
    window = MediaTrimmerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
