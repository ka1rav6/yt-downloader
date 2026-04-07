# YouTube Video Downloader

A simple web app to download YouTube videos quickly and easily.

## Features

* Download videos in multiple qualities (Best, 720p, 480p)
* Extract audio as MP3
* Clean and minimal UI
* Fast downloads using yt-dlp

## Tech Stack

* Python
* Streamlit
* yt-dlp

## Live App

https://video-yt-downloader.streamlit.app/

## Installation

Clone the repository:

```
git clone https://github.com/ka1rav6/yt-downloader.git
cd yt-downloader
```

Install dependencies using uv:

```
uv pip install -r requirements.txt
```

## Run Locally

```
streamlit run app.py
```
## Usage
1. Enter a YouTube URL
2. Select video quality
3. Choose output folder (local only)
4. Click download

## Notes

* Folder selection works only in local environment
* FFmpeg is required for audio downloads

Install FFmpeg:

```
sudo apt install ffmpeg
```
## License

This project is for educational purposes.
