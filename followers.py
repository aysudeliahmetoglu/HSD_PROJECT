
from bs4 import BeautifulSoup
from urllib.request import urlopen
handle="hsdyalova"
url='https://www.instagram.com/'
page=urlopen(url+handle).read()
soup=BeautifulSoup(page,"html.parser")
string=soup.find('meta',property="og:description")['data-content']
print(string)