import httpx
import re

def get_stream_url(url: str, pattern: str = "", is_turkuvaz: bool = False, verify: bool = True) -> str:
    """
    Unified function to fetch stream URLs from different sources.
    
    :url (str): The base URL to fetch from. For Turkuvaz streams, this should be the stream key.
    :pattern (str): Regex pattern to extract the stream URL.
    :is_turkuvaz (bool): If True, treats the url parameter as a Turkuvaz stream key.
    :return (str): The stream URL.
    """
    # Handle Turkuvaz URL construction
    if is_turkuvaz:
        url = f"http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/{url}/{url}.m3u8"
        pattern = r'"Url":"(.*?)"' if pattern == "" else pattern
    
    # Set default headers if none provided
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    
    # Add referer based on the type of stream
    if is_turkuvaz:
        headers['Referer'] = 'https://www.atv.com.tr/canli-yayin'
    else:
        headers['Origin'] = url
        headers['Referer'] = url
    
    # Send GET request
    response = httpx.get(url, headers=headers, verify=verify)
    
    # Remove backslashes from the response
    data = response.text.replace('\\', '')
    
    # Use regex to find the stream URL
    match = re.search(pattern, data)
    
    if match and match.group(1):
        stream_url = match.group(1)
        return stream_url
        
    raise Exception('Stream URL not found')
