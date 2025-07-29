# Media Trimmer Tool (PyQt5 + VLC)

A simple desktop media trimmer/converter built with **PyQt5**, **python-vlc**, and **ffmpeg**. This tool is built so I may save some time when searching for a website to trimmer/convert my media file.  
This project should support all video/audio format files. Please leave an issue if some of the format is not supported

---

## Features

- Load and play video files.
- Trim and export video clips using ffmpeg.
- convert media file to other format

---

## Requirements

- Python 3.x
- VLC Media Player (https://www.videolan.org/vlc/)
- FFmpeg (https://ffmpeg.org/download.html)
- Python dependencies:
  - PyQt5
  - python-vlc

---

## Installation & Setup

### 1. Download and run as an executable

Download the executable at [Releases](https://github.com/Misachu10032/Media-Trimmer/tree/main/release) page.  
Run the executable media_trimmer.exe

### 2. Run the code

#### Prerequisite

```bash
Download and Install Download VLC: https://www.videolan.org/vlc/
Download and Install Download FFmpeg: https://ffmpeg.org/download.html
```

#### Clone the Repository

```bash

git clone https://github.com/yourusername/media-trimmer.git
cd media-trimmer

#setup virtual env. this can be different for different os
venv\Scripts\activate
pip install PyQt5 python-vlc
```

#### Run the application

```bash
python src/media_trimmer/main.py
```
