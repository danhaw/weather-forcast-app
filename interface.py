from api_parser import ApiParser

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
        api = ApiParser(API_URL)
        api_data = api.get_all_data()
        #self.set_default_size(400, 400)
        box = Gtk.Box(spacing=10)
        self.add(box)
        grid = Gtk.Grid()
        grid.set_column_spacing(50)
        day1, grid = self.gen_single_data(grid)
        box.pack_start(grid, True, True, 0)
        for i in api_data[0]:
            day1["date"].set_text(i)
            day1["weather"].set_text(i)
            day1["weather_desc"].set_text(i)
            day1["wind_speed"].set_text(i)
            day1["wind_deg"].set_text(i)

        grid2 = Gtk.Grid()
        grid2.set_column_spacing(50)
        day1, grid2 = self.gen_single_data(grid2)
        box.pack_start(grid2, True, True, 0)

        grid3 = Gtk.Grid()
        grid3.set_column_spacing(50)
        day1, grid3 = self.gen_single_data(grid3)
        box.pack_start(grid3, True, True, 0)
        #self.add(grid)

        #button = Gtk.Button(label="refresh")
        #button.connect("clicked", self.refresh)
        #self.grid = Gtk.Grid()
        #self.grid.set_column_spacing(50)
        #grid.attach(label1, 0, 1, 1, 1)
        #grid.attach(label2, 0, 2, 1, 1)
        #grid.attach(label3, 0, 3, 1, 1)
        #self.grid.attach(button,3, 4 , 2, 1)
        #self.add(grid)
        
        #self.gen_labels()
    
    def gen_single_data(self, grid):
        lbl_dict = {}
        lbl_dict["date"] = Gtk.Label(label="value1")
        lbl_dict["weather"] = Gtk.Label(label="value2")
        lbl_dict["weather_desc"] = Gtk.Label(label="value3")
        lbl_dict["wind_speed"] = Gtk.Label(label="value3")
        lbl_dict["wind_deg"] = Gtk.Label(label="value3")
        
        grid.attach(lbl_dict["date"] ,        0, 1, 1, 1)
        grid.attach(lbl_dict["weather"],      0, 2, 1, 1)
        grid.attach(lbl_dict["weather_desc"], 0, 3, 1, 1)
        grid.attach(lbl_dict["wind_speed"],   0, 4, 1, 1)
        grid.attach(lbl_dict["wind_deg"],     0, 5, 1, 1)
        return (lbl_dict, grid)

    def gen_labels(self):
        """instead of making labels one by one 
        this method generated all the needed labels at once in a Gtk grid
        and it fill them with the data from the api"""
        api = ApiParser(API_URL)
        for i in range(5):
            self.grid.attach(Gtk.Label(label=next(api.get_all_data())),0, i, 1, 1) 
   
        #self.add(self.grid)

    def refresh(self, button):
        self.gen_labels()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()