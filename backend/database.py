<<<<<<< HEAD:backend/restaurants_db.py
import peewee
import csv
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

    with open('restaurants.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        restaurant_start=True
        for row in csv_reader: 
            if restaurant_start == True:
                rest=Restaurants.create(name=row[0],longitude= row[2], latitude=row[3],address= row[1],about=row[4])
                rest.save
                restaurant_start=False
            elif row[0]=='':
                restaurant_start=True
            else:
                men=Menu.create(restaurant_name=rest.id,menu_item=row[0], price=row[1])
                men.save



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