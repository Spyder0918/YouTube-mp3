# **YouTube to MP3 Converter** 🎶

This script takes a YouTube link, pulls the audio from the video, and saves it as an MP3 file. It automatically creates a folder called **`downloaded_audio`** (if not already present) and stores the MP3 there.

---

## **Features**
- **Download MP3** from YouTube videos
- Automatically **create a folder** for storing the audio (`downloaded_audio`)
- Supports high-quality MP3 audio extraction
- Easy to use and set up

---

## **Required Libraries**

This project uses two main libraries:

### **1. [MoviePy](https://github.com/Zulko/moviepy)**  
**MoviePy** is a powerful Python library for editing and processing videos. It allows you to:
- ✂️ **Cut**, **merge**, and edit videos
- 🎶 **Extract or add audio** to videos
- ✍️ **Add effects**, text, or overlays
- 🔄 **Convert between video formats**
- 🎥 **Work with GIFs** and image sequences

*Install it via pip:*  
`pip install moviepy`

## **2. yt-dlp**

**yt-dlp** is an open-source command-line tool that allows you to:

- 🎬 Download videos & audio from YouTube, Twitch, Twitter, and more
- 🛡️ Bypass ads & region restrictions
- 🎧 Extract audio as MP3
- 📜 Download playlists & subtitles
- ⚡ Better performance than youtube-dl

### **Install it via pip:**
`pip install yt-dlp`

## **3. FFmpeg**

**FFmpeg** is a multimedia framework that enables handling video/audio files and streams.

### **Why FFmpeg is needed:**
- 🔄 Convert video/audio files
- 🎧 Extract audio from video
- 🖥️ Process multimedia streams
- 🎬 Works well with MoviePy and yt-dlp

### **If FFmpeg is not already installed**, you may need to install it using Homebrew:
`brew install ffmpeg`

---

## **Setup Instructions**

1. **Clone this repository** to your local machine:
    `git clone https://github.com/your-username/youtube-to-mp3.git`


2. **Install the required libraries**:
    `pip install -r requirements.txt`
    

3. **Run the script** to download the MP3:
    `python youtube_mp3.py`
    or
    `python3 youtube_mp3.py`
  

4. Enter the **YouTube URL** when prompted, and your MP3 will be downloaded to the **`downloaded_audio`** folder!

---

## 🙌 **Contributions**

If you'd like to contribute to this project, feel free to:

- Fork the repository
- Create a pull request with improvements or bug fixes



