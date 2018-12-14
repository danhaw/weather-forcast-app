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
        self.set_default_size(400, 400)
        label1 = Gtk.Label(label="value1")
        label2 = Gtk.Label(label="value2")
        label3 = Gtk.Label(label="value3")
        
        button = Gtk.Button(label="refresh")
        button.connect("clicked", self.refresh)
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(50)
        #grid.attach(label1, 0, 1, 1, 1)
        #grid.attach(label2, 0, 2, 1, 1)
        #grid.attach(label3, 0, 3, 1, 1)
        self.grid.attach(button,3, 4 , 2, 1)
        self.gen_labels()
    
    def gen_labels(self):
        """instead of making labels one by one 
        this method generated all the needed labels at once in a Gtk grid
        and it fill them with the data from the api"""
        api = ApiParser(API_URL)
        for i in range(5):
            self.grid.attach(Gtk.Label(label=next(api.get_all_data())),0, i, 1, 1) 
   
        self.add(self.grid)

    def refresh(self, button):
        self.gen_labels()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()