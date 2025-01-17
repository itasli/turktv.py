from fastapi import APIRouter
from app.utils import ChannelRegistry, get_stream_url

turkuvaz_router = APIRouter(prefix="/turkuvaz", tags=["Turkuvaz Channels"])

ChannelRegistry.register_channel(
    name='ATV', 
    logo='https://i.ibb.co/CHhcZkv/atv-tr.png',
    order=1,
    url=get_stream_url('atvhd', is_turkuvaz=True),
    router=turkuvaz_router
)

ChannelRegistry.register_channel(
    name='ATV Avrupa', 
    logo='https://i.ibb.co/b7QcHw2/atv-avrupa-tr.png',
    order=2,
    url=get_stream_url('atvavrupa', is_turkuvaz=True),
    router=turkuvaz_router
)

ChannelRegistry.register_channel(
    name='A2', 
    logo='https://i.ibb.co/PcnS21c/a2-tr.png',
    order=3,
    url=get_stream_url('a2tv', is_turkuvaz=True),
    router=turkuvaz_router
)

ChannelRegistry.register_channel(
    name='A Haber', 
    logo='https://i.ibb.co/qrPmj32/a-haber-tr.png',
    order=4,
    url=get_stream_url('ahaberhd', is_turkuvaz=True),
    router=turkuvaz_router
)

ChannelRegistry.register_channel(
    name='A Para', 
    logo='https://i.ibb.co/gSfnN3R/a-para-tr.png',
    order=5,
    url=get_stream_url('aparahd', is_turkuvaz=True),
    router=turkuvaz_router
)

ChannelRegistry.register_channel(
    name='A Spor', 
    logo='https://i.ibb.co/55HnbJR/a-spor-tr.png',
    order=6,
    url=get_stream_url('asporhd', is_turkuvaz=True),
    router=turkuvaz_router
)

ChannelRegistry.register_channel(
    name='Minika Go', 
    logo='https://i.ibb.co/R77HGSg/minika-go-tr.png',
    order=7,
    url=get_stream_url('minikago', is_turkuvaz=True),
    router=turkuvaz_router
)

ChannelRegistry.register_channel(
    name='Minika Çocuk', 
    logo='https://i.ibb.co/zn5LrvM/minika-cocuk-tr.png',
    order=8,
    url=get_stream_url('minikacocuk', is_turkuvaz=True),
    router=turkuvaz_router
)


ChannelRegistry.update_resolvers(turkuvaz_router)
