from fastapi import APIRouter
from utils import ChannelRegistry

trt_router = APIRouter(prefix="/trt", tags=["TRT Channels"])

@ChannelRegistry.register_channel(
    name='TRT 1', 
    logo='https://i.ibb.co/xzSz0Pt/trt-1-tr.png',
    order=0
)
@trt_router.get("/trt1", name='TRT 1')
def resolve_trt1():
    return 'https://trt.daioncdn.net/trt-1/master.m3u8?app=web'


@ChannelRegistry.register_channel(
    name='TRT Diyanet Çocuk', 
    logo='https://i.ibb.co/k4rqCkb/trt-diyanet-cocuk.jpg',
    order=11.0
)
@trt_router.get("/trtdiyanetcocuk", name='TRT Diyanet Çocuk')
def resolve_trtdiyanetcocuk():
    return 'https://tv-trtdiyanetcocuk.medya.trt.com.tr/master.m3u8'


@ChannelRegistry.register_channel(
    name='TRT Çocuk', 
    logo='https://i.ibb.co/4tHc4fD/trt-cocuk-tr.png',
    order=11.0
)
@trt_router.get("/trtcocuk", name='TRT Diyanet Çocuk')
def resolve_trtcocuk():
    return 'http://tv-trtcocuk.medya.trt.com.tr/master.m3u8'


@ChannelRegistry.register_channel(
    name='TRT Haber', 
    logo='https://i.ibb.co/3kSXjwk/trt-haber-tr.png',
    order=2
)
@trt_router.get("/trthaber", name='TRT Haber')
def resolve_trthaber():
    return 'https://tv-trthaber.medya.trt.com.tr/master.m3u8'


@ChannelRegistry.register_channel(
    name='TRT Belgesel', 
    logo='https://i.ibb.co/pLNT9hC/trt-belgesel-tr.png',
    order=2
)
@trt_router.get("/trtbelgesel", name='TRT Belgesel')
def resolve_trtbelgesel():
    return 'https://tv-trtbelgesel.medya.trt.com.tr/master.m3u8'


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
