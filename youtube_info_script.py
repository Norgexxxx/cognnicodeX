import requests

def get_youtube_video_info(video_id):
    api_key = "AIzaSyDlAXXbfdxAapXB1v6LCsAN1Pwvm5wRwWg"

    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        json_data = response.json()

        video_details = json_data["items"][0]["snippet"]
        video_title = video_details["title"]
        video_description = video_details["description"]
        video_statistics = json_data["items"][0]["statistics"]
        view_count = video_statistics.get("viewCount", "N/A")
        like_count = video_statistics.get("likeCount", "N/A")
        comment_count = video_statistics.get("commentCount", "N/A")

        print("Video Title:", video_title)
        print("Video Description:", video_description)
        print("View Count:", view_count)
        print("Like Count:", like_count)
        print("Comment Count:", comment_count)

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

# Example usage
video_id_to_get_info = "kCc8FmEb1nY"
get_youtube_video_info(video_id_to_get_info)
