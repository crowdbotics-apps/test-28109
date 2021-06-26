from django.conf.urls import url

from .consumers import AlertsChannle
from django.urls import path

websocket_urlpatterns = [
    path('alerts/', AlertsChannle.as_asgi()),
    # path('chat/', Chat.as_asgi())
]
