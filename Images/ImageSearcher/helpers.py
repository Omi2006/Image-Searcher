from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def get_images(query):
    urls = []
    site = f"https://en.wikipedia.org/wiki/{query}"
    html = urlopen(site)
    bs = BeautifulSoup(html, "html.parser")
    images = bs.find_all("img", {"src":re.compile(".jpg")})
    for image in images:
        urls.append(image["src"])
    
    return urls, site


