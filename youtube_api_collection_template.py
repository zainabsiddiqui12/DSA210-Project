# YouTube Data API collection template
# Replace API_KEY and CHANNEL_IDS with real values before use.

import requests
import pandas as pd

API_KEY = "YOUR_API_KEY_HERE"
CHANNEL_IDS = [
    # "UCxxxxxxxx",
]

def get_upload_playlist_id(channel_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "contentDetails",
        "id": channel_id,
        "key": API_KEY
    }
    r = requests.get(url, params=params).json()
    return r["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

def get_playlist_items(playlist_id, max_results=30):
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "part": "snippet,contentDetails",
        "playlistId": playlist_id,
        "maxResults": max_results,
        "key": API_KEY
    }
    return requests.get(url, params=params).json()

def get_video_stats(video_ids):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "contentDetails,statistics,snippet",
        "id": ",".join(video_ids),
        "key": API_KEY
    }
    return requests.get(url, params=params).json()

# Suggested workflow:
# 1. For each channel, get upload playlist ID
# 2. Fetch the most recent 20-30 uploads
# 3. Extract upload date, duration, views, likes, comments
# 4. Save to CSV
