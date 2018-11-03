import sqlite3

def create_database():
    conn = sqlite3.connect("restaurants.db")

    c = conn.cursor()
    c.execute('''CREATE TABLE restaurants
        (restaurant_name text, longitude real, latitude real, address text, about text)''')
    c.execute('''CREATE TABLE menu
        (restaurant_name text, longitude real, latitude real, address text, about text)''')    
    conn.commit()
    conn.close()

def update_database():
    conn = sqlite3.connect("restarunts.db")
    c = conn.cursor()
    conn.commit()
    conn.close()
