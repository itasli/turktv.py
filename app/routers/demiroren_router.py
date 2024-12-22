from fastapi import APIRouter
from utils import ChannelRegistry

demiroren_router = APIRouter(prefix="/demiroren", tags=["Demiroren Channels"])

ChannelRegistry.register_channel(
    name='Kanal D', 
    logo='https://i.ibb.co/JdKh6Tq/kanal-d-tr.png',
    order=1,
    url="https://demiroren-live.daioncdn.net/kanald/kanald.m3u8",
    router=demiroren_router
)

ChannelRegistry.register_channel(
    name='Euro D', 
    logo='https://i.ibb.co/2NYV4Zn/euro-d-tr.png',
    order=1,
    url="https://kdlive.duhnet.tv/S2/HLS_LIVE/eurodnp/playlist.m3u8",
    router=demiroren_router
)

ChannelRegistry.register_channel(
    name='Teve 2', 
    logo='https://i.ibb.co/m8pLZK3/teve2-tr.png',
    order=1,
    url="https://demiroren.daioncdn.net/teve2/teve2.m3u8?ce=3&app=6aab838a-437e-4a1b-bbd0-e30f79cdbbbd",
    router=demiroren_router
)

ChannelRegistry.update_resolvers(demiroren_router)