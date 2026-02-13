import os
import subprocess
import shutil

SINGER_NAME = "Sharry Maan"
N_VIDEOS = 20
CLIP_SECONDS = 30
OUTPUT_FILE = "final_mashup.mp3"

if N_VIDEOS <= 10:
    raise ValueError("Number of videos must be greater than 10")

if CLIP_SECONDS <= 20:
    raise ValueError("Clip duration must be greater than 20 seconds")

for folder in ["videos", "audio", "trimmed"]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)
print("\n Downloading videos...\n")

download_command = [
    "yt-dlp",
    "--ignore-errors",
    "-f", "mp4",
    f"ytsearch{N_VIDEOS}:{SINGER_NAME}",
    "-o", "videos/%(id)s.%(ext)s"
]
subprocess.run(download_command)
print("\n Extracting audio...\n")

video_files = sorted(os.listdir("videos"))
for video in video_files:
    input_path = os.path.join("videos", video)
    output_path = os.path.join("audio", video.split(".")[0] + ".mp3")

    extract_command = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-vn",
        "-acodec", "mp3",
        output_path
    ]
    subprocess.run(extract_command)
print("\n✂ Trimming audio...\n")

audio_files = sorted(os.listdir("audio"))
for audio in audio_files:
    input_path = os.path.join("audio", audio)
    output_path = os.path.join("trimmed", audio)

    trim_command = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-t", str(CLIP_SECONDS),
        "-c", "copy",
        output_path
    ]
    subprocess.run(trim_command)
print("\n Merging all clips...\n")

with open("list.txt", "w") as file_list:
    trimmed_files = sorted(os.listdir("trimmed"))
    for file in trimmed_files:
        absolute_path = os.path.abspath(os.path.join("trimmed", file))
        file_list.write(f"file '{absolute_path}'\n")

merge_command = [
    "ffmpeg", "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", "list.txt",
    "-c", "copy",
    OUTPUT_FILE
]
subprocess.run(merge_command)
print("\n Mashup Created Successfully:", OUTPUT_FILE)