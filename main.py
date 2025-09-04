import requests
import time
import json
from typing import Dict, List

class TikTokFollowerBot:
    def __init__(self, session_id: str = None):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
        }
        
        if session_id:
            self.headers['Cookie'] = f'sessionid={session_id}'

    def follow_user(self, user_id: str) -> bool:
        """Follow a specific user"""
        url = f"https://www.tiktok.com/api/user/follow/{user_id}/"
        try:
            response = self.session.post(url, headers=self.headers)
            return response.status_code == 200
        except Exception as e:
            print(f"Error following user: {e}")
            return False

    def like_video(self, video_id: str) -> bool:
        """Like a specific video"""
        url = f"https://www.tiktok.com/api/comment/like/{video_id}/"
        try:
            response = self.session.post(url, headers=self.headers)
            return response.status_code == 200
        except Exception as e:
            print(f"Error liking video: {e}")
            return False

    def comment_on_video(self, video_id: str, comment: str) -> bool:
        """Post a comment on a video"""
        url = "https://www.tiktok.com/api/comment/publish/"
        data = {
            "text": comment,
            "aweme_id": video_id
        }
        try:
            response = self.session.post(url, json=data, headers=self.headers)
            return response.status_code == 200
        except Exception as e:
            print(f"Error commenting: {e}")
            return False

# Usage example
bot = TikTokFollowerBot("your_session_id_here")