import streamlit as st
import yt_dlp
import os
st.title("YouTube Downloader (yt-dlp)")
url = st.text_input("Enter YouTube URL")
quality = st.selectbox(
    "Select quality",
    ["Best", "720p", "480p", "Audio only"]
)
DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)
def get_ydl_opts(quality):
    if quality == "Best":
        return {'format': 'best', 'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s'}
    elif quality == "720p":
        return {'format': 'bestvideo[height<=720]+bestaudio/best', 'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s'}
    elif quality == "480p":
        return {'format': 'bestvideo[height<=480]+bestaudio/best', 'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s'}
    elif quality == "Audio only":
        return {
            'format': 'bestaudio/best',
            'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
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
            title = info.get('title', 'video')
            st.write(f"**Title:** {title}")
        if st.button("Download"):
            ydl_opts = get_ydl_opts(quality)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl: #type: ignore
                ydl.download([url])
            files = os.listdir(DOWNLOAD_DIR)
            latest_file = max(
                [os.path.join(DOWNLOAD_DIR, f) for f in files],
                key=os.path.getctime
            )
            st.success("Download completed!")
            with open(latest_file, "rb") as f:
                st.download_button(
                    label="Download File",
                    data=f,
                    file_name=os.path.basename(latest_file)
                )
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Enter a YouTube URL to begin")