from bs4 import BeautifulSoup

with open("../carviewer.html") as fp:
    soup = BeautifulSoup(fp,"html.parser")

# print out first occurence of tr inside the document
#print(soup.tr)
# go through all tr rows and and print them out
rows = soup.findAll("tr")

for row in rows:
    #print("----------")
    #print(row)
    dataList = []
    cols = row.findAll('td')
    for col in cols:
        dataList.append(col.text)
    print(dataList)


