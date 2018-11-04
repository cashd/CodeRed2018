from peewee import *
import csv
from geopy import distance

db = SqliteDatabase('/home/cash/Documents/CodeRed/CodeRed2018/backend/restaurants.db')

class Base(Model):
    class Meta:
        database = db

class Restaurants(Base):
    name = CharField()
    longitude = FloatField()
    latitude = FloatField()
    address = CharField()
    link = CharField()

class Menu(Base):
    restaurant = ForeignKeyField(Restaurants, on_delete='CASCADE')
    menu_item = CharField()
    price = CharField()
    category = CharField()

def create_database():
    db.create_tables([Restaurants, Menu])

def populate_test_data():
    db.create_tables([Restaurants, Menu])

    with open('restaurants.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        restaurant_start=True
        for row in csv_reader: 
            if restaurant_start == True:
                lng, lat = convert_address(row[1])
                rest=Restaurants.create(name=row[0],address= row[1], longitude= lng, latitude=lat,info=row[4],hours=row[5],link=row[6])
                rest.save
                restaurant_start=False
            elif row[0]=='':
                restaurant_start=True
            else:
                men=Menu.create(restaurant=rest.id,menu_item=row[0], price=row[1], info=row[2], category=row[3])
                men.save

# Gets all restraunt rows that are in range of the user
def get_rest_in_range(user_lat, user_long, max_range):
    restaurants = Restaurants.select()
    r_in_range = []
    for r in restaurants:
        user_coords = ( user_lat, user_long )
        rest_coords = ( r.latitude, r.longitude )
        if distance.distance(user_coords, rest_coords).miles <= max_range:
            r_in_range.append(r.id)

    return r_in_range


def get_response(user_lat, user_long, max_range, keyword):
    keyword = str(keyword)
    #Get rest in area
    db.connect()
    #rs = get_rest_in_range(user_lat, user_long, max_range)
    matches = Menu.select().where(Menu.menu_item.contains(keyword))
    final_matches = []
    j = []
    for m in matches:
        j.append(Restaurants.get(Restaurants.id == m.restaurant))
    print(len(j))
    for r in j:
        user_coords = ( user_lat, user_long )
        rest_coords = ( r.latitude, r.longitude )
        if distance.distance(user_coords, rest_coords).miles <= max_range:
            data = {
                "name": r.name,
                "dis": distance.distance(user_coords, rest_coords).miles,
                "address": r.address,
                "link": r.link,
                "lat": r.latitude,
                "long": r.longitude,
            }
            final_matches.append(data)
    result = [dict(t) for t in {tuple(d.items()) for d in final_matches}]
    return result
