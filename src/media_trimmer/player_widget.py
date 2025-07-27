import vlc
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
import sys

class VLCPlayer(QWidget):
    def __init__(self, video_frame, slider, status_label):
        super().__init__()
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.video_frame = video_frame
        self.slider = slider
        self.status_label = status_label
        
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_slider)

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

    def play(self):
        self.mediaplayer.play()
        self.timer.start()

    def pause(self):
        self.mediaplayer.pause()

    def update_slider(self):
        if self.mediaplayer.is_playing():
            pos = self.mediaplayer.get_position()
            self.slider.blockSignals(True)
            self.slider.setValue(int(pos * 1000))
            self.slider.blockSignals(False)

    def set_position(self, value):
        self.mediaplayer.set_position(value / 1000.0)
