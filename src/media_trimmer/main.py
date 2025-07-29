import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer
from media_trimmer.ui_mainwindow import Ui_MainWindow
from media_trimmer.player_widget import VLCPlayer
from media_trimmer.trimmer import trim_video as perform_trim_subprocess



class MediaTrimmerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI (controls and labels)
        self.ui = Ui_MainWindow(self)

        # Initialize VLCPlayer with UI components
        self.player = VLCPlayer(self.ui.video_frame, self.ui.status_label)

        # Connect the VLCPlayer signal for time updates to the method that updates the labels
        self.player.time_update_signal.connect(self.update_time_labels)

        # Connect buttons to player functions
        self.ui.load_button.clicked.connect(self.load_video)
        self.ui.play_pause_button.clicked.connect(self.player.toggle_play_pause)
        self.ui.jump_button.clicked.connect(self.jump_to_time)
        self.ui.set_start_time_button.clicked.connect(self.set_start_time)
        self.ui.set_end_time_button.clicked.connect(self.set_end_time)
        self.ui.reset_time_button.clicked.connect(self.reset_time_inputs)
        self.ui.trim_button.clicked.connect(self.trim_video)

        self.trim_start_ms = 0
        self.trim_end_ms = 0
        self.loaded_video_path = ""
        self.loaded_video_dir = ""
        self.loaded_video_name = ""
        self.loaded_video_basename = ""

    def load_video(self):
        # Open file dialog to load a video file
        filename, _ = QFileDialog.getOpenFileName(self, "Select Video")
        if filename:
            self.loaded_video_path = filename  # Full path to the file
            self.loaded_video_dir = os.path.dirname(filename)  # Folder path
            self.loaded_video_name = os.path.basename(
                filename
            )  # File name with extension
            self.loaded_video_basename = os.path.splitext(self.loaded_video_name)[
                0
            ]  # File name without extension

            self.ui.status_label.setText(f"Loaded: {self.loaded_video_name}")
            self.player.set_media(filename)

    def update_time_labels(self, current_time, total_time):
        """Update the time labels with the current and total time."""
        current_time_str = self.format_time(current_time)
        total_time_str = self.format_time(total_time)

        self.ui.current_time_label.setText(f"Current Time: {current_time_str}")
        if total_time == -1:
            self.ui.total_time_label.setText(f"Total Time: loaded")
        else:
            self.ui.total_time_label.setText(f"Total Time: {total_time_str}")

    def format_time(self, time_in_ms):
        """Convert time in milliseconds to hh:mm:ss.ms format."""
        total_seconds = time_in_ms // 1000
        hours = total_seconds // 3600  # 3600 seconds in an hour
        total_seconds %= 3600  # Remainder after hours
        minutes = total_seconds // 60  # Calculate minutes
        seconds = total_seconds % 60  # Remaining seconds
        milliseconds = time_in_ms % 1000  # Get milliseconds part

        return f"{int(hours)}:{int(minutes):02}:{int(seconds):02}.{int(milliseconds / 10):02}"

    def get_time_from_inputs(self):
        """Helper function to extract time from input fields and convert to milliseconds."""
        try:
            hours = int(self.ui.hour_input.text() or 0)
            minutes = int(self.ui.minute_input.text() or 0)
            seconds = int(self.ui.second_input.text() or 0)
            milliseconds = int(self.ui.millisecond_input.text() or 0)

            # Convert time to milliseconds
            total_time_ms = (
                hours * 3600 + minutes * 60 + seconds
            ) * 1000 + milliseconds
            return total_time_ms
        except ValueError:
            self.ui.status_label.setText("Invalid input. Please enter numbers.")
            return None

    def jump_to_time(self):
        """Get time from input fields and jump to the specified time."""
        try:
            total_time_ms = self.get_time_from_inputs()
            # Ensure media is playing (seek won't work if stopped)
            print(total_time_ms, "_____-------------")
            if not self.player.mediaplayer.is_playing():
                self.player.mediaplayer.play()
                # Delay the seek slightly to let VLC start playback
                QTimer.singleShot(
                    200, lambda: self.player.mediaplayer.set_time(total_time_ms)
                )
            else:
                self.player.mediaplayer.set_time(total_time_ms)

            self.ui.status_label.setText(
                f"Jumped to: {self.format_time(total_time_ms)}"
            )
        except ValueError:
            self.ui.status_label.setText("Invalid input. Please enter numbers.")

    def set_start_time(self):
        """Capture user input as trim start time."""
        total_time_ms = self.get_time_from_inputs()
        if total_time_ms is not None:
            self.trim_start_ms = total_time_ms  # Save start time
            formatted_time = self.format_time(total_time_ms)
            self.ui.trim_start_time.setText(f"Trim Start Time: {formatted_time}")
            self.ui.status_label.setText("Start time set.")

    def set_end_time(self):
        """Capture user input as trim end time."""
        total_time_ms = self.get_time_from_inputs()
        if total_time_ms is not None:
            self.trim_end_ms = total_time_ms  # Save end time
            formatted_time = self.format_time(total_time_ms)
            self.ui.trim_end_time.setText(f"Trim End Time: {formatted_time}")
            self.ui.status_label.setText("End time set.")

    def reset_time_inputs(self):
        """Reset all time input fields to 0."""
        self.ui.hour_input.setText("0")
        self.ui.minute_input.setText("0")
        self.ui.second_input.setText("0")
        self.ui.millisecond_input.setText("0")
        self.ui.status_label.setText("Time inputs reset to 0.")

    def trim_video(self):
        if not self.loaded_video_path:
            self.ui.status_label.setText("No video loaded.")
            return

        if self.trim_end_ms <= self.trim_start_ms:
            self.ui.status_label.setText("Invalid trim range.")
            return

        # Call trimmer function

        output_path = perform_trim_subprocess(
            input_file=self.loaded_video_path,
            output_dir=self.loaded_video_dir,
            base_name=self.loaded_video_basename,
            start_time_ms=self.trim_start_ms,
            end_time_ms=self.trim_end_ms,
        )
        self.ui.status_label.setText(f"Trimmed video saved: {output_path}")


def main():
    app = QApplication(sys.argv)
    window = MediaTrimmerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
