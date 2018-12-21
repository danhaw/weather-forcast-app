from api_parser import ApiParser
from db import DB
import scripts

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

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)
        self.display_all_data(api_data)
        


        refresh_btn = Gtk.Button(label="refresh")
        self.box.pack_start(refresh_btn, True, True, 0)
        refresh_btn.connect("clicked", self.refresh)
        
        
    def display_all_data(self, api_data):
        '''here I set the the data that I got from the database to the labels text,
        then display them in the grid '''
        kel_to_c = lambda k: round(k - 273.15) #this lambda function convert from Kelvin to Celsius 
        for i in [0, 10, 17, 25]:
            grid = Gtk.Grid()
            grid.set_column_spacing(50)
            self.box.pack_start(grid, True, True, 0)
            day, grid = self._display_single_data(grid)
            day["temp"].set_text(str(kel_to_c(api_data[i][0]))+ '°')
            day["date"].set_text(str(api_data[i][1]))
            day["weather"].set_text(str(api_data[i][2]))
            day["weather_desc"].set_text(str(api_data[i][3]))
            day["wind_speed"].set_text(str(api_data[i][4]))
            day["wind_deg"].set_text(str(api_data[i][5]))

    def _display_single_data(self, grid):
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


    def refresh(self, button):
        scripts.clear_db()
        scripts.fill_db()

        #getting data from the database
        db_data = DB("data.db") 
        api_data = db_data.get_all_data()

        #displaying the data in the window
        self.display_all_data(api_data)



win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()