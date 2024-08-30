from urllib.parse import urljoin
from urllib.parse import urlparse


def url_formater(soup, path, host, site_name):
    for script in soup.find_all("script", src=True):
        src = script["src"]
        absolute_url = urljoin(path, src)
        if urlparse(absolute_url).netloc == urlparse(path).netloc:
            script["src"] = urljoin(urlparse(absolute_url).netloc, src)

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        absolute_url = urljoin(path, href)
        if urlparse(absolute_url).netloc == urlparse(path).netloc:
            a_tag["href"] = f"{host}proxy/{site_name}/{absolute_url}"

    for use in soup.find_all("use", href=True):
        href = use["href"]
        absolute_url = urljoin(path, href)

        if urlparse(absolute_url).netloc == urlparse(path).netloc:
            use["href"] = f"{host}proxy/{site_name}/{href}"

        if use.has_attr("xlink:href"):
            xlink_href = use["xlink:href"]
            absolute_url = urljoin(path, xlink_href)
            if urlparse(absolute_url).netloc == urlparse(path).netloc:
                use["xlink:href"] = urljoin(urlparse(absolute_url).netloc, xlink_href)

    for link_tag in soup.find_all("link", href=True):
        href = link_tag["href"]
        absolute_url = urljoin(path, href)
        if urlparse(absolute_url).netloc == urlparse(path).netloc:
            link_tag["href"] = absolute_url

    for script in soup.find_all("script", src=True):
        src = script["src"]
        absolute_url = urljoin(path, src)
        if urlparse(absolute_url).netloc == urlparse(path).netloc:
            script["src"] = absolute_url

    for img in soup.find_all("img"):
        if img.has_attr("src"):
            src = img["src"]
            absolute_url_src = urljoin(path, src)
            if urlparse(absolute_url_src).netloc == urlparse(path).netloc:
                img["src"] = absolute_url_src
        if img.has_attr("href"):
            href = img["href"]
            absolute_url_href = urljoin(path, href)
            if urlparse(absolute_url_href).netloc == urlparse(path).netloc:
                img["src"] = absolute_url_href
    return soup
