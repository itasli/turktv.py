from fastapi import APIRouter
from app.utils import ChannelRegistry

trt_router = APIRouter(prefix="/trt", tags=["TRT Channels"])

ChannelRegistry.register_channel(
    name='TRT 1', 
    logo='https://i.ibb.co/xzSz0Pt/trt-1-tr.png',
    order=0,
    url='https://trt.daioncdn.net/trt-1/master.m3u8?app=web',
    router=trt_router
)

ChannelRegistry.register_channel(
    name='TRT Diyanet Çocuk', 
    logo='https://i.ibb.co/k4rqCkb/trt-diyanet-cocuk.jpg',
    order=11.0,
    url='https://tv-trtdiyanetcocuk.medya.trt.com.tr/master.m3u8',
    router=trt_router
)

ChannelRegistry.register_channel(
    name='TRT Çocuk', 
    logo='https://i.ibb.co/4tHc4fD/trt-cocuk-tr.png',
    order=11.0,
    url='http://tv-trtcocuk.medya.trt.com.tr/master.m3u8',
    router=trt_router
)


ChannelRegistry.register_channel(
    name='TRT Haber', 
    logo='https://i.ibb.co/3kSXjwk/trt-haber-tr.png',
    order=2,
    url='https://tv-trthaber.medya.trt.com.tr/master.m3u8',
    router=trt_router
)


ChannelRegistry.register_channel(
    name='TRT Belgesel', 
    logo='https://i.ibb.co/pLNT9hC/trt-belgesel-tr.png',
    order=2,
    url='https://tv-trtbelgesel.medya.trt.com.tr/master.m3u8',
    router=trt_router
)


ChannelRegistry.update_resolvers(trt_router)
