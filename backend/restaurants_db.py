import peewee
from peewee import *
 
"""
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
    conn = sqlite3.connect("restaurants.db")
    c = conn.cursor()
    conn.commit()
    conn.close()

create_database()
"""

db = SqliteDatabase('restaurants.db')

class Base(Model):
    class Meta:
        database = db

class Restaurants(Base):
    name = CharField()
    longitude = FloatField()
    latitude = FloatField()
    address = CharField()
    about = CharField()

class Menu(Base):
    name = CharField()
    menu_item = CharField()
    price = DoubleField()

db.connect()
db.create_tables([Restaurants, Menu])
