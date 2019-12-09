import requests, json
from xlwt import *

url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()

w = Workbook()
ws = w.add_sheet('followers')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"repos_url")

row += 1
for x in data:
    ws.write(row,0, x["login"])
    ws.write(row,1,x["repos_url"])
    
    row += 1
w.save('githubusers.xls')