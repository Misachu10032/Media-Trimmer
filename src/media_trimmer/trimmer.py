# FFmpeg trimming logic
import subprocess

def trim_video(input_file, output_file, start_time, end_time):
    command = [
        'ffmpeg',
        '-y',  # Overwrite output file if exists
        '-i', input_file,
        '-ss', str(start_time),
        '-to', str(end_time),
        '-c', 'copy',
        output_file
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
