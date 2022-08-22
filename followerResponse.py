import urllib.request
import json
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from appJar import gui

##### EXPORT #####
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


client = gspread.authorize(creds)

sheet = client.open("somestats").sheet1

##### FUNCTIONS #####
def makeGUI():
    global fb
    global total


    # Instagram
    app.startLabelFrame("Instagram", 0, 1)
    app.addImage("Instagram", "img/Instagram.gif")
    app.addLabel("Instagram", "Followers: " + str(ig))
    app.stopLabelFrame()

def exportToDrive():
    # Get date and time
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    #Insert data to the first data column in the sheet
    insertRow = [now, yt, fb, ig, tv, t, total]
    sheet.insert_row(insertRow, 2)

##### INIT #####
app = gui("Social Media Total Followers", "720x720")
app.setBg("white")
app.setFont(15)



def exportToDrive():
    # Get date and time
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    #Insert data to the first data column in the sheet
    insertRow = [now, yt, fb, ig, tv, t, total]
    sheet.insert_row(insertRow, 2)
##### INSTAGRAM #####
#Instagram username
igID = ""   

igdata = urllib.request.urlopen("https://www.instagram.com/" + igID + "/?__a=1").read()
ig = json.loads(igdata)["graphql"]["user"]["edge_followed_by"]["count"]
app.go()