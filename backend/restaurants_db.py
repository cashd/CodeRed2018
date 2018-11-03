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
    name = ForeignKeyField(Restaurants,on_delete='CASCADE')
    menu_item = CharField()
    price = DoubleField()

def populate_test_data():
    db.create_tables([Restaurants, Menu])
    for i in range(10):
        Restaurants.create(name='pizza hut',longitude= 2.6, latitude=3.6,address= 'Enchanted',about='Spring')

db.connect()
populate_test_data()
