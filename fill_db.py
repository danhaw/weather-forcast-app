from db import DB
from  api_parser import ApiParser

with open("api_key.txt") as f:
    api_key = f.read()
API_URL = "http://api.openweathermap.org/data/2.5/forecast?q=London,us&appid={}".format(api_key)

db = DB("data.db")

api = ApiParser(API_URL)
api_data = api.get_all_data()

for item in api.get_all_data():
    db.Add_data(item[0], item[1], item[2], item[3], item[4], item[5])

