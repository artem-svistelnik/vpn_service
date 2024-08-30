from django.urls import path
from service.views import *

app_name = "service"

urlpatterns = [
    path("<str:site_name>/<path:path>", proxy_view, name="proxy-view"),
]
