from fastapi import APIRouter
from app.utils import ChannelRegistry, get_stream_url

cinergroup_router = APIRouter(prefix="/cinergroup", tags=["Cinergroup Channels"])

ChannelRegistry.register_channel(
    name='Show TV', 
    logo='https://i.ibb.co/GckcgJ0/show-tr.png',
    order=1,
    url=get_stream_url('https://www.showtv.com.tr/canli-yayin', r'videoUrl\s*=\s*"(.*?)"'),
    router=cinergroup_router
)

ChannelRegistry.register_channel(
    name='Show Max', 
    logo='https://i.ibb.co/gmjC3x1/show-max-tr.png',
    order=1,
    url=get_stream_url('http://showmax.com.tr/canliyayin', r'"ht_stream_m3u8":"(.*?)"'),
    router=cinergroup_router
)

ChannelRegistry.register_channel(
    name='Show Türk', 
    logo='https://i.ibb.co/yBKG9kH/show-turk-tr.png',
    order=1,
    url=get_stream_url('https://www.showturk.com.tr/canli-yayin', r'"ht_stream_m3u8":"(.*?)"'),
    router=cinergroup_router
)

ChannelRegistry.register_channel(
    name='Habertürk', 
    logo='https://i.ibb.co/Jpx3g3R/haberturk-tr.png',
    order=1,
    url=get_stream_url('https://www.haberturk.com/canliyayin', r'videoUrl = "(.*?)"'),
    router=cinergroup_router
)

ChannelRegistry.register_channel(
    name='Bloomberght', 
    logo='https://i.ibb.co/DrCRwJV/bloomberg-ht-tr.png',
    order=1,
    #url=get_cinergroup_stream('https://www.bloomberght.com/tv', r'videoUrl = "(.*?)"'),
    router=cinergroup_router,
    disabled=True
)


ChannelRegistry.update_resolvers(cinergroup_router)
