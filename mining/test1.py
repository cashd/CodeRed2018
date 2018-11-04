import requests
from bs4 import BeautifulSoup
import re

alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))
alphabet.append("1")

fileout = open("companylinks.txt", "w+")

init_URL = "https://www.menuwithprice.com/location/texas/houston/"

def locate_rest(s):
    links = s.find_all("a", href=True)
    x = []
    for l in links:
        x.append(l['href'])
    #Regexing over all the links
    r = re.compile("^https:\\/\\/www.menuwithprice.com\\/menu\\/([A-Za-z0-9]-?)*\\/texas\\/houston")
    #filtered_links = set(filter(r.match, links))
    links = list(filter(r.match, x))
    for s in links:
        fileout.write(s+"\n")

r2 = requests.get('https://www.menuwithprice.com/location/texas/houston/a/p/1/')
soup2 = BeautifulSoup(r2.content, features="html.parser")
locate_rest(soup2)

for place in alphabet:
    num = 1;
    alpha_URL = init_URL + str(place) + "/p/" + str(num)+ "/"
    r1 = requests.get(alpha_URL)
    soup1 = BeautifulSoup(r1.content, features="html.parser")
    locate_rest(soup1)
    num += 1
    alpha_URL = init_URL + str(place) + "/p/" + str(num)+ "/"
    r1 = requests.get(alpha_URL)
    while r1.status_code != 404:
        alpha_URL = init_URL + str(place) + "/p/" + str(num)+ "/"
        r1 = requests.get(alpha_URL)
        soup1 = BeautifulSoup(r1.content, features="html.parser")
        locate_rest(soup1)
        num += 1
        alpha_URL = init_URL + str(place) + "/p/" + str(num)+ "/"
        r1 = requests.get(alpha_URL)
        

fileout.close()


r = requests.get('https://www.menuwithprice.com/menu/chipotle-mexican-grill/texas/houston/27807/')

soup = BeautifulSoup(r.content, features="html.parser")

contents = soup.find_all("tr", class_="prc-th")
contents2 = soup.find_all("tr")

category = ""

for con in contents2:
    if(len(con.contents)>=2):
        print(con.contents[0].string,con.contents[1].string,category,con.contents[2].string)
    else:
        category = con.contents[0].string
        