def generate_playlist(channels: dict, base_url: str) -> str:
    """
    Generates a dynamic M3U file based on the provided channels
    
    :param channels: Dictionary of channels
    :param base_url: Base URL for the resolvers
    :return: M3U file content
    """
    m3u_content = '#EXTM3U\n'
    for key, channel in channels.items():
        # Prepare optional attributes
        logo_part = f' tvg-logo="{channel["logo"]}"' if channel.get('logo') else ''
        
        # Construct M3U entry
        m3u_content += (
            f'#EXTINF:-1 '
            f'tvg-id="{key}" '
            f'tvg-name="{channel["name"]}"{logo_part},'
            f'{channel["name"]}\n'
        )

        # Add resolver URL if available
        if channel.get('resolver'):
            m3u_content += f'{base_url}{channel["resolver"]}\n'

    return m3u_content

def save_playlist(playlist_content: str, filename: str = 'playlist.m3u', encoding: str = 'utf-8') -> None:
    """
    Saves playlist content to a file
    
    :param playlist_content: M3U file content
    :param filename: Output filename
    :param encoding: File encoding
    """
    try:
        with open(filename, 'w', encoding=encoding) as f:
            f.write(playlist_content)
        print(f"Playlist M3U generated successfully: {filename}")
    except IOError as e:
        print(f"Error saving playlist: {e}")