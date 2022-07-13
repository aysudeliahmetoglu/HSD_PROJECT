from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
 
URL="https://www.instagram.com/"

def get_data(username):
    last_url=URL + username

    request= Request(last_url,headers={'User-Agent':'Mozilla/5.0'})
    html_data = urlopen(request).read()

    soup=BeautifulSoup(html_data,'html.parser')
    data = soup.find("meta",property="og:description").attrs['content']
    data = data.split("-")[0]

    data = data.split("-")
    print("followers: " +data[0])
    print("following: " +data[2])
    print("posts: " +data[4])
    

username = input("please enter username: ")    
get_data(username)

