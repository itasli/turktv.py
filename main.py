from fastapi import FastAPI, Response, Request
from routers import trt_router, turkuvaz_router, cinergroup_router
from utils import ChannelRegistry, generate_playlist

app = FastAPI(title="turktv.py")

# Register routers
app.include_router(trt_router)
app.include_router(turkuvaz_router)
app.include_router(cinergroup_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/playlist.m3u")
async def get_playlist(r : Request):
    """
    Generate full M3U playlist

    :param r: Request object
    :return: M3U file content
    """
    base_url = str(r.base_url).strip('/')
    channels = ChannelRegistry.get_channels()
    playlist_content = generate_playlist(channels, base_url)
    
    # Return playlist_content
    return Response(playlist_content, media_type='application/x-mpegurl', headers={'Content-Disposition': 'attachment; filename=playlist.m3u'})

@app.get("/channel/{channel_name}")
async def get_channel(channel_name: str):
    """
    Get specific channel details

    :param channel_name: Channel name
    :return: Channel information
    """
    channel = ChannelRegistry.get_channel(channel_name)
    if channel:
        return channel
    return {"error": "Channel not found"}
