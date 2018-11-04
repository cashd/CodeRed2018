from peewee import *
from geopy import distance
import os

db = SqliteDatabase('/home/cash/Documents/CodeRed/CodeRed2018/backend/restaurants.db')

class Base(Model):
    class Meta:
        database = db

class Restaurants(Base):
    name = CharField()
    longitude = FloatField()
    latitude = FloatField()
    address = CharField()
    info = CharField()
    link = CharField()

class Menu(Base):
    restaurant = ForeignKeyField(Restaurants, on_delete='CASCADE')
    menu_item = CharField()
    price = DoubleField()
    info = CharField()
    catagory = CharField()


def create_database():
    db.create_tables([Restaurants, Menu])

def populate_test_data():
    db.connect()
    db.create_tables([Restaurants, Menu])
    #for i in range(10):
    Restaurants.create(name='Pizza Hut',longitude= 2.6, latitude=3.6,address= 'Enchanted',about='Spring')
    Restaurants.create(name='Dominoes',longitude= 2.6, latitude=3.6,address= 'Enchanted',about='Spring')
    Restaurants.create(name='Pizza Hut',longitude= 2.5, latitude=4.6,address= 'Enchanted',about='Spring')
    # for i in range(10):
    Menu.create(restaurant_name=id,menu_item='pizza', price=5.5)
    Menu.create(restaurant_name=Restaurants.get(name="Pizza Hut"),menu_item='wings', price=10.5)
    Menu.create(restaurant_name=Restaurants.get(name="Pizza Hut"),menu_item='pasta', price=6)
    Menu.create(restaurant_name=Restaurants.get(name="Dominoes"),menu_item='pizza', price=5.5)
    Menu.create(restaurant_name=Restaurants.get(name="Dominoes"),menu_item='wings', price=10.5)
    Menu.create(restaurant_name=Restaurants.get(name="Dominoes"),menu_item='pasta', price=6)


# Gets all restraunt rows that are in range of the user
def get_rest_in_range(user_lat, user_long, max_range):
    db.connect()
    restaurants = Restaurants.select()
    print(len(restaurants))
    r_in_range = []
    for r in restaurants:
        user_coords = ( user_lat, user_long )
        rest_coords = ( r.latitude, r.longitude )
        print(user_coords, rest_coords)
        print(distance.distance(user_coords, rest_coords).miles)
        if distance.distance(user_coords, rest_coords).miles <= max_range:
            r_in_range.append(r.name)

    return r_in_range