from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
 
URL="https://www.instagram.com/"

def get_data(username):
    last_url=URL + username

    request= Request(last_url,headers={'User-Agent':'Mozilla/5.0'})
    html_data = urlopen(request).read()

    soup=BeautifulSoup(html_data,'html.parser')
    data=soup.find("meta",property="og:description").attrs['content']