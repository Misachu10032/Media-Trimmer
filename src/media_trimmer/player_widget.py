import vlc
from PyQt5.QtCore import QTimer, pyqtSignal, QObject  # Import QObject
import sys


class VLCPlayer(QObject):
    time_update_signal = pyqtSignal(int, int)

    def __init__(self, video_frame, status_label):
        super().__init__()
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.video_frame = video_frame
        self.status_label = status_label

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_time)  # <-- Connect timer to updater

    def set_media(self, filepath):
        media = self.instance.media_new(filepath)
        self.mediaplayer.set_media(media)

        if sys.platform == "win32":
            self.mediaplayer.set_hwnd(int(self.video_frame.winId()))
        elif sys.platform == "linux":
            self.mediaplayer.set_xwindow(int(self.video_frame.winId()))
        elif sys.platform == "darwin":
            self.mediaplayer.set_nsobject(int(self.video_frame.winId()))

        # Emit initial total time after parsing

        self.time_update_signal.emit(0, -1)


    def toggle_play_pause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()  # Pause the media if it's playing
            self.timer.stop()  # Stop the timer when paused
        else:
            self.mediaplayer.play()  # Play the media if it's paused
            self.timer.start()  # Start the timer when playing

    def update_time(self):
        current_time = self.mediaplayer.get_time()
        total_time = self.mediaplayer.get_length()
        if current_time != -1 and total_time > 0:
            self.time_update_signal.emit(current_time, total_time)
