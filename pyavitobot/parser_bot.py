"""
!!!Данная версия проекта является тестовой!!!
"""

import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs

URL = ''
r = rq.get(URL)
resbs = bs(r.text, 'html.parser')
html = resbs.find_all('a')

for i in html:
    print(i)