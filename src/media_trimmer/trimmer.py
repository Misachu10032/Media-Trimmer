import os
import subprocess

def trim_video(input_file, output_dir, base_name, start_time_ms, end_time_ms):
    # Convert milliseconds to seconds (float)
    start_seconds = start_time_ms / 1000
    duration_seconds = (end_time_ms - start_time_ms) / 1000

    # Generate a unique output filename
    counter = 1
    output_filename = f"{base_name}_trimmed_{counter}.mp4"
    output_path = os.path.join(output_dir, output_filename)

    while os.path.exists(output_path):
        counter += 1
        output_filename = f"{base_name}_trimmed_{counter}.mp4"
        output_path = os.path.join(output_dir, output_filename)

    # FFmpeg command
    command = [
        "ffmpeg",
        "-y",  # Overwrite without asking
        "-i", input_file,
        "-ss", str(start_seconds),
        "-t", str(duration_seconds),
        "-c:v", "copy",
        "-c:a", "copy",
        output_path
    ]

    # Execute FFmpeg
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return output_path
