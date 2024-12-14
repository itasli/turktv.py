import requests
import re

def get_turkuvaz_stream(key):
    """
    Fetch stream URL for a given key from the video token service.
    
    :param key: Stream key
    :return: Stream URL
    """
    url = f"http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/{key}/{key}.m3u8"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Referer': 'https://www.atv.com.tr/canli-yayin',
    }
    
    # Send GET request
    response = requests.get(url, headers=headers)
    
    # Remove backslashes from the response
    data = response.text.replace('\\', '')
    
    # Use regex to find the stream URL
    pattern = r'"Url":"(.*?)"'
    match = re.search(pattern, data)
    
    if match and match.group(1):
        stream_url = match.group(1)
        return stream_url
    
    raise Exception('Stream URL not found')
