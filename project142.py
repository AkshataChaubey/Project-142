import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
scrappingpage=requests.get(url)
print(scrappingpage)
# print("akshata")
Soup=BeautifulSoup(scrappingpage.text,"html.parser")
# print(Soup)
startable=Soup.find_all("table")
# print(startable)
datalist=[]

tablerows=startable[7].find_all("tr")
# print(tablerows)
for tr in tablerows:
    td=tr.find_all("td")
    # print(td)
    data=[i.text.rstrip()for i in td]
    # print(data)
    datalist.append(data)
starname=[]
stardistance=[]
starmass=[]
starradius=[]    

# print(datalist)
# ['SDSS J000013.54+255418.6\xa0[de]', 'Pegasus', '0h 0m 13.54s', '25°\xa054′\xa018″', '', '46.1', 'T4.5', '48', '0.99', '2004'],name=1
for i in range(1,len(datalist)):
    starname.append(datalist[i][1])
    stardistance.append(datalist[i][5])
    starmass.append(datalist[i][7])
    starradius.append(datalist[i][8])
    
file=pd.DataFrame(list(zip(starname,stardistance,starmass,starradius)),columns=["starname","stardistance","starmass","starradius"])   
file.to_csv("dwarfstar.csv") 
print(len(datalist))

    
