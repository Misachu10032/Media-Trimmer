import vlc
from PyQt5.QtCore import QTimer, pyqtSignal, QObject  # Import QObject
import sys


class VLCPlayer(QObject):  # Make VLCPlayer inherit from QObject
    # Signal to update time labels
    time_update_signal = pyqtSignal(int, int)  # Signal format: (current_time, total_time)

    def __init__(self, video_frame, slider, status_label):
        super().__init__()  # Call the constructor of QObject
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.video_frame = video_frame
        self.slider = slider
        self.status_label = status_label
        
        self.timer = QTimer()
        self.timer.setInterval(500)  # Update every 500 ms

        # Connect the slider to the set_position method
        self.slider.valueChanged.connect(self.set_position)

    def set_media(self, filepath):
        media = self.instance.media_new(filepath)
        self.mediaplayer.set_media(media)

        # OS-specific video frame binding
        if sys.platform == "win32":
            self.mediaplayer.set_hwnd(int(self.video_frame.winId()))
        elif sys.platform == "linux":
            self.mediaplayer.set_xwindow(int(self.video_frame.winId()))
        elif sys.platform == "darwin":
            self.mediaplayer.set_nsobject(int(self.video_frame.winId()))

        # Set the total time for the video
        total_time = self.mediaplayer.get_length()
        self.slider.setMaximum(total_time)
        self.time_update_signal.emit(0, total_time)  # Emit signal to update total time label

    def play(self):
        self.mediaplayer.play()
        self.timer.start()

    def pause(self):
        self.mediaplayer.pause()
        self.timer.stop()

    def set_position(self, value):
        self.mediaplayer.set_time(value)  # Update the player position based on slider value
