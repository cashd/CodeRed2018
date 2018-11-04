import requests
import csv
from bs4 import BeautifulSoup

def mine_menu():
    reslinks = open("restaurantlinks.txt", "r")
    
    
    
    for line in reslinks:
        try:
            compURL = line.replace('\n', '')
            print(compURL)
            r = requests.get(compURL)
        
            soup = BeautifulSoup(r.content, features="html.parser")

            contents2 = soup.find_all("tr")
            contents3 = soup.find("h1")
            name = contents3.find("span")

            contents4 = soup.find("li", {"id": "dt-addr"})
            addy = contents4.find('a')

            contents6 = soup.find("li", {"id": "dt-menu"})
            menlink = contents6.find('a')
            csvRow = [name.text,addy.text.replace(',', ''),menlink['href']]
            with open("foods.csv","a", newline='', encoding="utf-8") as csvfile:
                rest_writer=csv.writer(csvfile)
                rest_writer.writerow(csvRow)

            category = ""

            for con in contents2:
            
                if(len(con.contents)>=2):
                    csvRow = [con.contents[0].string, con.contents[1].string, category, con.contents[2].string]
                    with open("foods.csv","a", newline='', encoding="utf-8") as csvfile:
                        rest_writer=csv.writer(csvfile)
                        rest_writer.writerow(csvRow)

                else:
                    category = con.contents[0].string
            with open("foods.csv","a", newline='', encoding="utf-8") as csvfile:
                rest_writer=csv.writer(csvfile)
                rest_writer.writerow([])
        except:
            pass
  
    reslinks.close()

mine_menu()