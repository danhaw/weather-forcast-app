import sqlite3 
import sys 

class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = None
    
    def _connect(self):
        """a helper method for connecting to the database"""
        try:
            self.con = sqlite3.connect(self.db_name)
            return None
        except sqlite3.Error as e:
            return "Error {}:".format(e.args[0])
            
    
    def Add_data(self, date_txt, weather, weather_desc, wind_speed, wind_deg):
        """this method adds the concerned data to the database"""
        con_err = self._connect()
        if not con_err:
            cur = self.con.cursor()
            cur.execute("INSERT INTO dates(date_txt, weather, weather_desc, wind_speed, wind_deg) VALUES(?, ?, ?, ?, ?)", (date_txt, weather, weather_desc, wind_speed, wind_deg))
            self.con.commit()
        else:
            return con_err

    def get_all_data(self):
        """this method gets the concerned data from the database"""                
        con_err = self._connect()
        if not con_err:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM dates")
            return cur.fetchall()
        else:
             return con_err 










