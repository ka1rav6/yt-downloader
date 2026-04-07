import streamlit as st
import yt_dlp
import os

st.title("YouTube Downloader (yt-dlp)")
url = st.text_input("Enter YouTube URL")

quality = st.selectbox(
    "Select quality",
    ["Best", "720p", "480p", "Audio only"]
)
output_folder = st.text_input("Enter download folder path", "downloads")
def get_ydl_opts(quality, folder):
    if quality == "Best":
        return {
            'format': 'best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s'
        }
    elif quality == "720p":
        return {
            'format': 'bestvideo[height<=720]+bestaudio/best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s'
        }
    elif quality == "480p":
        return {
            'format': 'bestvideo[height<=480]+bestaudio/best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s'
        }
    elif quality == "Audio only":
        return {
            'format': 'bestaudio/best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

if url:
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            st.write(f"**Title:** {info.get('title', 'Unknown Title')}")
        if st.button("Download"):
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            ydl_opts = get_ydl_opts(quality, output_folder)
            if ydl_opts is not None:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl: #type: ignore
                    ydl.download([url])
                st.success("Download completed!")
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Enter a YouTube URL to begin")