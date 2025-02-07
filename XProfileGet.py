import requests
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

def get_image_profile(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        profile_image_get = data['data']['profile_image_url']
        high_res_url = profile_image_get.replace('_normal', '_400x400')
        return high_res_url
    else:
        return "Error: Invalid username or API issue"

username = input('Enter profile username: ')
profile_get_url = get_image_profile(username)
print(f'User profile image URL:\n {profile_get_url}')