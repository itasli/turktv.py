from fastapi import APIRouter
from utils import ChannelRegistry

trt_router = APIRouter(prefix="/trt", tags=["TRT Channels"])

@ChannelRegistry.register_channel(
    name='TRT 1', 
    logo='http://example.com/trt1-logo.png',
    order=0
)
@trt_router.get("/trt1", name='TRT 1')
def resolve_trt1():
    return 'https://trt.daioncdn.net/trt-1/master.m3u8?app=web'


@ChannelRegistry.register_channel(
    name='TRT Diyanet Çocuk', 
    logo='http://example.com/trt2-logo.png',
    order=11.0
)
@trt_router.get("/trtdiyanetcocuk", name='TRT Diyanet Çocuk')
def resolve_trtdiyanetcocuk():
    return 'https://tv-trtdiyanetcocuk.medya.trt.com.tr/master.m3u8'


@ChannelRegistry.register_channel(
    name='TRT Haber', 
    logo='http://example.com/trthaber-logo.png',
    order=2
)
@trt_router.get("/trthaber", name='TRT Haber')
def resolve_trthaber():
    return 'https://tv-trthaber.medya.trt.com.tr/master.m3u8'


@trt_router.get("/channel/{channel_name}")
async def get_trt_channel(channel_name: str):
    """
    Get specific TRT channel details

    :param channel_name: Channel name
    :return: Channel information
    """
    channel = ChannelRegistry.get_channel(channel_name)
    if channel:
        return channel
    return {"error": "Channel not found"}

ChannelRegistry.update_resolvers(trt_router)
