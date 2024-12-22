from fastapi import APIRouter
from utils import ChannelRegistry

dogus_router = APIRouter(prefix="/dogus", tags=["Dogus Channels"])

ChannelRegistry.register_channel(
    name='Star TV', 
    logo='https://i.ibb.co/gjfbcyg/star-tv-tr.png',
    order=1,
    url="https://dogus-live.daioncdn.net/startv/startv.m3u8",
    router=dogus_router
)

ChannelRegistry.register_channel(
    name='Eurostar', 
    logo='https://i.ibb.co/ZWpVp8V/euro-star-tr.png',
    order=1,
    url="http://dygvideo.dygdigital.com/live/hls/staravrupa?token=dc804d19951a5d69b6119b9d28b03c82c6981f1e33091f8a",
    router=dogus_router
)

ChannelRegistry.register_channel(
    name='NTV', 
    logo='https://i.ibb.co/c2yFHDv/ntv-tr.png',
    order=2,
    url="https://dogus-live.daioncdn.net/ntv/ntv.m3u8",
    router=dogus_router
)

ChannelRegistry.register_channel(
    name='DMAX', 
    logo='https://i.ibb.co/412LJ1F/dmax.png',
    order=3,
    url="https://dogus-live.daioncdn.net/dmax/dmax.m3u8",
    router=dogus_router
)

ChannelRegistry.register_channel(
    name='TLC', 
    logo='https://i.ibb.co/yFLGpmC/tlc.png',
    order=3,
    url="https://dogus-live.daioncdn.net/tlc/tlc.m3u8",
    router=dogus_router
)

ChannelRegistry.update_resolvers(dogus_router)