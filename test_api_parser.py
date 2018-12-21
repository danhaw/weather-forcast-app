import unittest
import api_parser


#getting the api key
with open("api_key.txt") as f:
    api_key = f.read()


API_URL = "http://api.openweathermap.org/data/2.5/forecast?q=London,us&appid={}".format(api_key)
api = api_parser.ApiParser(API_URL)

class TestApiParser(unittest.TestCase):

    def test_request(self):
        self.assertNotEqual(api._request(), None)
        self.assertEqual(type(api._request()), type(dict()))


    def test_get_list(self):
        self.assertNotEqual(api._get_list(), None)
        self.assertEqual(type(api._get_list()), type(list()))

    




    def test_get_weathers(self):
        self.assertNotEqual(api.get_weathers(), None)
        self.assertEqual(type(api.get_weathers()), type(list()))
        for item in api.get_weathers():
            self.assertEqual(type(item), type(tuple()))
            self.assertEqual(type(item[0]), type(str()))
            self.assertEqual(len(item[0]), 19)
            self.assertEqual(type(item), type(tuple()))
            self.assertEqual("main" in item[1][0], True)
            self.assertEqual("description" in item[1][0], True)
    
    
    def test_get_winds(self):
        self.assertNotEqual(api.get_winds(), None)
        self.assertEqual(type(api.get_winds()), type(list()))
        for item in api.get_winds():
            self.assertEqual(type(item), type(tuple()))
            self.assertEqual("speed" in item[1], True)
            self.assertEqual("deg" in item[1], True)
    

    def test_get_temperature(self):
        self.assertNotEqual(api.get_temperature(), None)
        self.assertEqual(type(api.get_temperature()), type(list()))
        for item in api.get_temperature():
            self.assertEqual(type(item), type(tuple()))
            self.assertEqual("temp" in item[1], True)
            self.assertEqual("pressure" in item[1], True)

    def test_get_all_data(self):
        self.assertNotEqual(next(api.get_all_data()), None)
        self.assertEqual(type(next(api.get_all_data())), type(tuple()))


if __name__ == '__main__':
    unittest.main()


