#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3 as db

con = db.connect("data.db")

with con:
    cur = con.cursor()
    #create the table
    cur.execute("CREATE TABLE dates(temp FLOAT, date_txt TEXT, weather TEXT, weather_desc TEXT, wind_speed FLAOT, wind_deg FLOAT  INT)")

