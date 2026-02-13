# Mashup--Assignment

# YouTube Mashup Generator

##  Project Overview

This project is developed as part of the Mashup Assignment.

The system performs the following operations:

1. Downloads N YouTube videos of a given singer.
2. Extracts audio from each video.
3. Trims the first Y seconds from each audio file.
4. Merges all trimmed clips into a single mashup file.
5. Provides both:
   - Command Line Interface (Program 1)
   - Web Application with Email Delivery (Program 2)

---

#  Program 1 – Command Line Mashup

##  Description

This program accepts user input from the command line and:

- Downloads top N videos of a singer from YouTube
- Converts them to MP3
- Trims first Y seconds
- Merges all clips into one final output file

---

##  Usage

```bash
python <RollNumber>.py <SingerName> <NumberOfVideos> <Duration> <OutputFile>
