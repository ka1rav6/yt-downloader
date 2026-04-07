import streamlit as st
import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog
def get_directory():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    root.destroy()
    return folder_path
st.title("YouTube Downloader (yt-dlp)")
url = st.text_input("Enter YouTube URL")

quality = st.selectbox(
    "Select quality",
    ["Best", "720p", "480p", "Audio only"]
)
if "output_folder" not in st.session_state:
    st.session_state.output_folder = ""
if st.button("Select Folder"):
    st.session_state.output_folder = get_directory()
if st.session_state.output_folder:
    st.write("Directory path:", st.session_state.output_folder)
def get_ydl_opts(quality, folder):
    if quality == "Best":
        return {'format': 'best', 'outtmpl': f'{folder}/%(title)s.%(ext)s'}
    elif quality == "720p":
        return {'format': 'bestvideo[height<=720]+bestaudio/best', 'outtmpl': f'{folder}/%(title)s.%(ext)s'}
    elif quality == "480p":
        return {'format': 'bestvideo[height<=480]+bestaudio/best', 'outtmpl': f'{folder}/%(title)s.%(ext)s'}
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
            folder = st.session_state.output_folder
            if not folder:
                st.error("Please select a folder first!")
            else:
                if not os.path.exists(folder):
                    os.makedirs(folder)
                ydl_opts = get_ydl_opts(quality, folder)
                with yt_dlp.YoutubeDL(ydl_opts) as ydl: #type: ignore
                    ydl.download([url])

                st.success("Download completed!")

    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Enter a YouTube URL to begin")