import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://finance.yahoo.com/q?s=tsla')

html = response.read()

soup = BeautifulSoup(html)

full_span = soup.find_all('span', {'id':'yfs_l84_tsla'})
#more robust way to not choke on empty lists
for spans in full_span:
    for content in spans.contents:
        print(content)


