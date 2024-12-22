from fastapi import FastAPI, Response, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import trt_router, turkuvaz_router, cinergroup_router, demiroren_router, dogus_router
from utils import ChannelRegistry, generate_playlist

app = FastAPI(title="turktv.py")

# Register routers
app.include_router(trt_router)
app.include_router(turkuvaz_router)
app.include_router(cinergroup_router)
app.include_router(demiroren_router)
app.include_router(dogus_router)

# Register static files
app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/")
async def read_root():
    """
    Root endpoint

    :return: Hello World
    """
    return Response(content="Hello World", media_type='text/html')

@app.get("/favicon.ico")
async def get_favicon():
    """
    Get favicon

    :return: Favicon file
    """
    return FileResponse("public/favicon.ico")

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
    return Response(status_code=404, content="Channel not found")
