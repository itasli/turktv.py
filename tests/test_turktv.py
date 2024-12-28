from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# Check the root endpoint
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello World"

# Check playlist.m3u endpoint
def test_playlist_endpoint():
    """Test the response headers and content of the playlist endpoint"""
    response = client.get("/playlist.m3u")
    
    # Verify response metadata
    assert response.status_code == 200, "Expected 200 OK status code"
    assert response.headers["content-type"] == 'application/x-mpegurl', "Invalid content type"
    assert response.headers["content-disposition"] == 'attachment; filename=playlist.m3u', "Invalid content disposition"
    
    # 2. Get response content
    content = response.text
    lines = content.strip().split('\n')
    
    # 3. Verify basic M3U structure
    assert lines[0] == '#EXTM3U', "File should start with #EXTM3U"
    
    # 4. Verify channel entries
    for i in range(1, len(lines), 2):  # Check pairs of lines (info + URL)
        if i + 1 >= len(lines):
            break
            
        info_line = lines[i]
        url_line = lines[i + 1]
        
        # Verify EXTINF line format
        assert info_line.startswith('#EXTINF:-1'), f"Invalid channel info format at line {i}"
        assert 'tvg-id="' in info_line, f"Missing tvg-id at line {i}"
        assert 'tvg-name="' in info_line, f"Missing tvg-name at line {i}"
        
        # Verify channel name is present (after comma)
        assert ',' in info_line, f"Missing channel name delimiter at line {i}"
        
        # Verify URL line
        assert url_line.strip(), f"Empty URL at line {i + 1}"
        assert url_line.startswith('http://') or url_line.startswith('https://'), f"Invalid URL format at line {i + 1}"
