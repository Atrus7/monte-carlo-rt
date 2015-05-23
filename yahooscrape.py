import urllib.request
from bs4 import BeautifulSoup

responce = urllib.request.urlopen('http://google.com')

html = responce.read()

soup = BeautifulSoup(html)

print(soup.find_all('span', {'id':'yfs_l84_tsla'}))
