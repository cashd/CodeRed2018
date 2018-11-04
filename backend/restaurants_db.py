import peewee
import csv
from peewee import *

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
    restaurant_name = ForeignKeyField(Restaurants,on_delete='CASCADE')
    menu_item = CharField()
    price = DoubleField()



def populate_test_data():
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


db.connect()
populate_test_data()