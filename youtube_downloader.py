#!/usr/bin/python3

import yt_dlp

# Enter the URL
url = input("Enter the URL to your Youtube video: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")
