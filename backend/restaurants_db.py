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
    restaurant_name = ForeignKeyField(Restaurants,on_delete='CASCADE')
    menu_item = CharField()
    price = DoubleField()



def populate_test_data():
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

db.connect()
populate_test_data()