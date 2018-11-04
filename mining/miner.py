import requests
from bs4 import BeautifulSoup

# Takes in a text file with company links and returns a
# text file with the specifc links to mine
def mine_location_links():
    clinks = open("companylinks.txt", "r")
    reslinks = open("restaurantlinks.txt", "w+")
    for line in clinks:
        compURL = line.replace('\n', '')
        r = requests.get(compURL)
        soup = BeautifulSoup(r.content, features="html.parser")

        contents = soup.find_all("table", {"class": "stores-list"})
        for con in contents:
            divs = con.find_all('tr')
            for div in divs:
                reflink = div.find_all('td')
                for indx in reflink:
                    t1 = indx.find_all('a')
                    for ts in t1:
                        reslinks.write(ts['href']+"\n")
                        print(ts['href'])
    clinks.close()
    reslinks.close()                       
 

# main
mine_location_links()