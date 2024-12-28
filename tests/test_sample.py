from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# Test to check the root endpoint
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello World"

# Test to check playlist.m3u file returned
def test_playlist_endpoint_headers():
    """Test the response headers of the playlist endpoint"""
    response = client.get("/playlist.m3u")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == 'application/x-mpegurl'
    assert response.headers["content-disposition"] == 'attachment; filename=playlist.m3u'

# Test to check playlist.m3u file is correct
def test_playlist_content():
    response = client.get("/playlist.m3u")
    assert response.status_code == 200
    assert response.headers['content-disposition'] == 'attachment; filename=playlist.m3u'
    assert response.headers['content-type'] == 'application/x-mpegurl'
    assert "#EXTM3U" in response.text
    assert "#EXTINF" in response.text