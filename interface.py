from api_parser import ApiParser
from db import DB

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#getting the api key
with open("api_key.txt") as f:
    api_key = f.read()




API_URL = "http://api.openweathermap.org/data/2.5/forecast?q=London,us&appid={}".format(api_key)
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Weather Forcast 0.1")
        
        #getting data from the database
        db_data = DB("data.db") 
        api_data = db_data.get_all_data()

        box = Gtk.Box(spacing=10)
        self.add(box)

        #this lambda function convert from Kelvin to Celsius 
        kel_to_c = lambda k: round(k - 273.15) 

        #there is a better way to do this for sure but I don't know enough of Gtk+ :')
        #here I set the the data that I got from the database to the labels text  
        grid = Gtk.Grid()
        grid.set_column_spacing(50)
        day1, grid = self.gen_single_data(grid)
        box.pack_start(grid, True, True, 0)   
        day1["temp"].set_text(str(kel_to_c(api_data[0][0]))+ '°')
        day1["date"].set_text(str(api_data[0][1]))
        day1["weather"].set_text(str(api_data[0][2]))
        day1["weather_desc"].set_text(str(api_data[0][3]))
        day1["wind_speed"].set_text(str(api_data[0][4]))
        day1["wind_deg"].set_text(str(api_data[0][5]))

        grid2 = Gtk.Grid()
        grid2.set_column_spacing(50)
        day2, grid2 = self.gen_single_data(grid2)
        box.pack_start(grid2, True, True, 0)
        day2["temp"].set_text(str(kel_to_c(api_data[10][0]))+ '°')
        day2["date"].set_text(str(api_data[10][1]))
        day2["weather"].set_text(str(api_data[10][2]))
        day2["weather_desc"].set_text(str(api_data[10][3]))
        day2["wind_speed"].set_text(str(api_data[10][4]))
        day2["wind_deg"].set_text(str(api_data[10][5]))


        grid3 = Gtk.Grid()
        grid3.set_column_spacing(50)
        day3, grid3 = self.gen_single_data(grid3)
        box.pack_start(grid3, True, True, 0)
        day3["temp"].set_text(str(kel_to_c(api_data[17][0]))+ '°')
        day3["date"].set_text(str(api_data[17][1]))
        day3["weather"].set_text(str(api_data[17][2]))
        day3["weather_desc"].set_text(str(api_data[17][3]))
        day3["wind_speed"].set_text(str(api_data[17][4]))
        day3["wind_deg"].set_text(str(api_data[17][5]))
        
        grid4 = Gtk.Grid()
        grid4.set_column_spacing(50)
        day4, grid4 = self.gen_single_data(grid4)
        box.pack_start(grid4, True, True, 0)
        day4["temp"].set_text(str(kel_to_c(api_data[25][0]))+ '°')
        day4["date"].set_text(str(api_data[25][1]))
        day4["weather"].set_text(str(api_data[25][2]))
        day4["weather_desc"].set_text(str(api_data[25][3]))
        day4["wind_speed"].set_text(str(api_data[25][4]))
        day4["wind_deg"].set_text(str(api_data[25][5]))

        refresh_btn = Gtk.Button(label="refresh")
        box.pack_start(refresh_btn, True, True, 0)
        
        
    
    def gen_single_data(self, grid):
        """this method generate the required labels
         and put them in the grid then it returns thier handles and the modified grid"""
        lbl_dict = {}
        lbl_dict["temp"] = Gtk.Label(label="value1")
        lbl_dict["date"] = Gtk.Label(label="value1")
        lbl_dict["weather"] = Gtk.Label(label="value2")
        lbl_dict["weather_desc"] = Gtk.Label(label="value3")
        lbl_dict["wind_speed"] = Gtk.Label(label="value3")
        lbl_dict["wind_deg"] = Gtk.Label(label="value3")
        
        grid.attach(lbl_dict["date"] ,        0, 1, 1, 1)
        grid.attach(lbl_dict["temp"] ,        0, 2, 1, 1)
        grid.attach(lbl_dict["weather"],      0, 3, 1, 1)
        grid.attach(lbl_dict["weather_desc"], 0, 4, 1, 1)
        grid.attach(lbl_dict["wind_speed"],   0, 5, 1, 1)
        grid.attach(lbl_dict["wind_deg"],     0, 6, 1, 1)
        return (lbl_dict, grid)

    #def gen_labels(self):
    #   """instead of making labels one by one 
    #    this method generated all the needed labels at once in a Gtk grid
    #    and it fill them with the data from the api"""
    #    api = ApiParser(API_URL)
    #    for i in range(5):
    #    self.grid.attach(Gtk.Label(label=next(api.get_all_data())),0, i, 1, 1) 
    #
    #    self.add(self.grid)
    #
    #def refresh(self, button):
    #   self.gen_labels()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()