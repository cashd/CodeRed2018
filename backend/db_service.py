import requests
import json

def convert_address(location):
    api_key = "AIzaSyA71w-QBNhPJfqVovLnhskJbgtHhHFwuaI"

    address = location.split(" ")
    address = "+".join(word for word in address)
    geocoding_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + api_key
    geocoding_data = requests.get(geocoding_url)
    geocoding_json = json.loads(geocoding_data.text)

    latitude = geocoding_json['results'][0]['geometry']['location']['lat']
    longitude = geocoding_json['results'][0]['geometry']['location']['lng']

    return longitude, latitude

def convert_coordinates(longitude, latitude):
    api_key = "AIzaSyA71w-QBNhPJfqVovLnhskJbgtHhHFwuaI"

    geocoding_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(latitude) + ',' + str(longitude) + '&key=' + api_key
    geocoding_data = requests.get(geocoding_url)
    geocoding_json = json.loads(geocoding_data.text)

    print(geocoding_url)
    address = geocoding_json['results'][0]['formatted_address']

    return address