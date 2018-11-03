import peewee
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
    name = CharField()
    menu_item = CharField()
    price = DoubleField()

db.connect()
db.create_tables([Restaurants, Menu])
