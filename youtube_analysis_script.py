import urllib.request

def connect_to_internet(url):
    try:
        # Open the URL and read the content
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
            print("Connected to the internet successfully.")
            print("Content from the provided URL:")
            print(html_content.decode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")

def connect_to_youtube(api_key, video_id):
    try:
        # Example YouTube API request
        youtube_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,contentDetails,statistics,status"
        connect_to_internet(youtube_url)

    except Exception as e:
        print(f"Error connecting to YouTube: {e}")

def read_video(local_video_path):
    try:
        # Placeholder for reading local video file
        print(f"Reading local video file: {local_video_path}")

    except Exception as e:
        print(f"Error reading local video: {e}")

# Example usage
url_to_connect = "https://www.youtube.com/watch?v=kCc8FmEb1nY"
youtube_api_key = "AIzaSyDlAXXbfdxAapXB1v6LCsAN1Pwvm5wRwWg"
youtube_video_id = url_to_connect.split("v=")[1]  # Extract video ID from YouTube URL
local_video_path = "path/to/your/local/video.mp4"

connect_to_internet(url_to_connect)
connect_to_youtube(youtube_api_key, youtube_video_id)
read_video(local_video_path)
