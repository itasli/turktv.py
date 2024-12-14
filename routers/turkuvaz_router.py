from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from utils import ChannelRegistry, get_turkuvaz_stream

turkuvaz_router = APIRouter(prefix="/turkuvaz", tags=["Turkuvaz Channels"])

@ChannelRegistry.register_channel(
    name='ATV', 
    logo='https://i.ibb.co/CHhcZkv/atv-tr.png',
    order=1
)
@turkuvaz_router.get("/atv", name='ATV', response_class=RedirectResponse)
def resolve_atv():
    return get_turkuvaz_stream('atvhd')


@ChannelRegistry.register_channel(
    name='ATV Avrupa', 
    logo='https://i.ibb.co/b7QcHw2/atv-avrupa-tr.png',
    order=2
)
@turkuvaz_router.get("/atvavrupa", name='ATV Avrupa', response_class=RedirectResponse)
def resolve_atv_avrupa():
    return get_turkuvaz_stream('atvavrupa')


@ChannelRegistry.register_channel(
    name='A2', 
    logo='https://i.ibb.co/PcnS21c/a2-tr.png',
    order=3
)
@turkuvaz_router.get("/a2", name='A2', response_class=RedirectResponse)
def resolve_a2():
    return get_turkuvaz_stream('a2tv')


@ChannelRegistry.register_channel(
    name='A Haber', 
    logo='https://i.ibb.co/qrPmj32/a-haber-tr.png',
    order=4
)
@turkuvaz_router.get("/ahaber", name='A Haber', response_class=RedirectResponse)
def resolve_ahaber():
    return get_turkuvaz_stream('ahaberhd')


@ChannelRegistry.register_channel(
    name='A Para', 
    logo='https://i.ibb.co/gSfnN3R/a-para-tr.png',
    order=5
)
@turkuvaz_router.get("/apara", name='A Para', response_class=RedirectResponse)
def resolve_apara():
    return get_turkuvaz_stream('aparahd')


@ChannelRegistry.register_channel(
    name='A Spor', 
    logo='https://i.ibb.co/55HnbJR/a-spor-tr.png',
    order=6
)
@turkuvaz_router.get("/aspor", name='A Spor', response_class=RedirectResponse)
def resolve_aspor():
    return get_turkuvaz_stream('asporhd')


@ChannelRegistry.register_channel(
    name='Minika Go', 
    logo='https://i.ibb.co/R77HGSg/minika-go-tr.png',
    order=7
)
@turkuvaz_router.get("/minikago", name='Minika Go', response_class=RedirectResponse)
def resolve_minikago():
    return get_turkuvaz_stream('minikago')


@ChannelRegistry.register_channel(
    name='Minika Çocuk', 
    logo='https://i.ibb.co/zn5LrvM/minika-cocuk-tr.png',
    order=8
)
@turkuvaz_router.get("/minikacocuk", name='Minika Çocuk', response_class=RedirectResponse)
def resolve_minikacocuk():
    return get_turkuvaz_stream('minikagococuk')

ChannelRegistry.update_resolvers(turkuvaz_router)
