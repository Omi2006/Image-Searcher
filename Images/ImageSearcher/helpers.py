from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def get_images(url, query=None):
    urls = []
    if query is not None:
        query = query.split()
        sanitized_query = "-".join(query)
        site = f"{url}/{sanitized_query}"
    
    else:
        site = url

    print(site)
    try:
        html = urlopen(site)
    except:
        return "Url not found", site
    bs = BeautifulSoup(html, "html.parser")
    images = bs.find_all("img", {"src":re.compile(".jpg")})
    for image in images:
        urls.append(image["src"])
    
    return urls, site


