from fastapi import APIRouter
from app.utils import ChannelRegistry, get_stream_url

others_router = APIRouter(prefix="/others", tags=["Others Channels"])

ChannelRegistry.register_channel(
    name='NOW', 
    logo='https://i.ibb.co/MNNfH78/now-tr.png',
    order=1,
    url=get_stream_url('https://www.nowtv.com.tr/canli-yayin', r"daiUrl : '(.*?)'", verify=False),
    router=others_router
)

ChannelRegistry.update_resolvers(others_router)