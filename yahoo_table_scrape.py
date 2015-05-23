# **********************Author Info**************************
# *@author    Christopher Findeisen                         *
# *@contact    <cfindeisen7@gmail.com>                      *
# *@date     Sat 23 May 15:20:25 2015                       *
# ***********************************************************
import sys #for arg parsing
import urllib.request
from bs4 import BeautifulSoup as BS

#callable with python [prog_name].py [name_of_column]
#start argument parsing
#note that argv[0] will be the name of the py program
if(len(sys.argv) > 1):
    column_name = sys.argv[1]

else:
    column_name = 'Adj Close*' #default column


#begin web parsing
response = urllib.request.urlopen('http://finance.yahoo.com/q/hp?s=TSLA+Historical+Prices')

html = response.read()
soup = BS(html)

index_we_want = None
head_check = soup.find_all('th', {'class':'yfnc_tablehead1'})
for i, th in enumerate(head_check):
    for content in th.contents:
        #note:we were choking on some hidden whitespace, which we kill with strip()
        if content.strip() == column_name:
            index_we_want = i

result = soup.find_all('td', {'class':'yfnc_tabledata1'})
for i, td in enumerate(result):
    if(i % len(head_check) == index_we_want):
        for contents in td.contents:
            print(contents)

