from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib.auth.decorators import login_required

from helpers.url_formater import url_formater
from .models import Site
from django.http import HttpResponse

import requests

User = get_user_model()


@login_required
def proxy_view(request, site_name, path):
    site = Site.objects.filter(name=site_name, user=request.user).first()
    if not site or site.user != request.user:
        raise Http404("Site not found")
    try:
        host = request.build_absolute_uri("/")
        site.increment_visit_count()
        response = requests.get(path)
        data_received = len(response.content)

        soup = BeautifulSoup(response.content, "html.parser")
        soup = url_formater(soup, path, host, site_name)

        content_type = response.headers["content-type"]
        modified_content = str(soup)

        data_sent = len(modified_content.encode("utf-8"))
        site.update_data_usage(data_sent, data_received)
        user = User.objects.get(id=request.user.id)
        user.update_data_usage(data_sent, data_received)

        return HttpResponse(modified_content, content_type=content_type)

    except requests.RequestException as e:
        return HttpResponse(str(e), status=500)
