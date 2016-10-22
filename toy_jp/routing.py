# In routing.py
# from channels.routing import route
# channel_routing = [
#     route("http.request", "my_consumers.my_consumers.http_consumer"),
# ]

from channels.routing import route
from my_consumers.my_consumers import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
]