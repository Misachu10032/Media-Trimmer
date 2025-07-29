# Media Trimmer Tool (PyQt5 + VLC)

A simple desktop video trimmer built with **PyQt5**, **python-vlc**, and **ffmpeg**. This tool allows users to load videos, jump to specific timestamps, set start and end trim points, and export trimmed video segments.

---

## Features
- Load and play video files.
- Input timestamp (HH:MM:SS.MS) to jump to a specific time.
- Set start and end trim points from user inputs.
- Trim and export video clips using ffmpeg.
- Avoid overwriting by auto-numbering output files.
- Simple and minimal UI.

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

### Clone the Repository
```bash
git clone https://github.com/yourusername/media-trimmer.git
cd media-trimmer
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

## Runing the application
python src/media_trimmer/main.py