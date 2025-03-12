import os
import yt_dlp #pytube can be used but has issued

# Function to download audio from a YouTube video and save it as an MP3
def download_audio(youtube_url, downloaded_audio):
    try:
        # Create the 'downloaded_audio' folder if it doesn't exist
        if not os.path.exists(downloaded_audio):
            os.makedirs(downloaded_audio)
            print(f"Created folder: {downloaded_audio}")
        
        # Define yt-dlp options for audio extraction
        ydl_opts = {
            'format': 'bestaudio/best',  # Best audio format
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(downloaded_audio, '%(title)s.%(ext)s'),
        }
        
        # Download the audio
        print("Downloading the audio...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        
        print("Audio successfully downloaded and saved.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to prompt user for YouTube URL and download folder
def main():
    youtube_url = input("Enter the YouTube video URL: ")
    download_folder = "downloaded_audio"  # Folder name is fixed to 'downloaded_audio'
    download_audio(youtube_url, download_folder)

if __name__ == "__main__":
    main()
