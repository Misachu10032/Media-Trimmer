import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
from media_trimmer.ui_mainwindow import Ui_MainWindow
from media_trimmer.player_widget import VLCPlayer
from media_trimmer.trimmer import trim_video

class MediaTrimmerApp(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.player = VLCPlayer(self.video_frame, self.slider, self.status_label)
        self.filepath = ""

        self.load_button.clicked.connect(self.load_video)
        self.play_button.clicked.connect(self.player.play)
        self.pause_button.clicked.connect(self.player.pause)
        self.slider.valueChanged.connect(self.player.set_position)
        self.trim_button.clicked.connect(self.trim_selection)

    def load_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Video")
        if filename:
            self.filepath = filename
            self.player.set_media(filename)
            self.status_label.setText(f"Loaded: {filename}")

    def trim_selection(self):
        if not self.filepath:
            self.status_label.setText("No video loaded!")
            return

        start_time = 5  # Seconds (You can extend UI to select these dynamically)
        end_time = 15   # Seconds
        output_file = "trimmed_output.mp4"

        trim_video(self.filepath, output_file, start_time, end_time)
        self.status_label.setText(f"Trimmed video saved as: {output_file}")

def main():
    app = QApplication(sys.argv)
    window = MediaTrimmerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
