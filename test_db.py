import unittest
import db
import os
import sqlite3 

# con = sqlite3.connect("test_data.db")

# with con:
#     cur = con.cursor()
#     #create the table
#     cur.execute("CREATE TABLE IF NOT EXISTS dates(temp FLOAT, date_txt TEXT, weather TEXT, weather_desc TEXT, wind_speed FLAOT, wind_deg FLOAT  INT)")





# data = db.DB("test_data.db")



# class TestDB(unittest.TestCase):

#     def test_add_data(self):
#         data.Add_data(278.81, '2018-12-26 09:00:00', 'Rain', 'light rain', 2.61, 224.502)
#         con = data._connect()
#         with con:
#             cur = data.con.cursor()
#             cur.execute("SELECT * FROM dates")
#             result =  cur.fetchall()  
#         self.assertEqual(result, [(278.81, '2018-12-26 09:00:00', 'Rain', 'light rain', 2.61, 224.502)])

#     def test_get_all_data(self):
#         pass
#         # con = data._connect()
#         # with con:
#         #     cur = data.con.cursor()
#         #     cur.execute("INSERT INTO dates(temp, date_txt, weather, weather_desc, wind_speed, wind_deg) VALUES(?, ?, ?, ?, ?, ?)", (data.Add_data(269.412, '2018-12-25 06:00:00', 'Clouds', 'few clouds', 1.67, 194.003)))
#         #     data.con.commit()       
#         # self.assertEqual(data.get_all_data(), [(278.81, '2018-12-26 09:00:00', 'Rain', 'light rain', 2.61, 224.502), (278.81, '2018-12-26 09:00:00', 'Rain', 'light rain', 2.61, 224.502)])


#     def test_clear_data(self):
#         data.clear_data()
#         self.assertEqual(data.get_all_data(), [])

# os.remove("test_data.db")

# if __name__ == '__main__':
#     unittest.main()