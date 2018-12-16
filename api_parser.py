import requests

class ApiError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class ApiParser():
    def __init__(self, api_url):
        self.url = api_url
        self._dates_lst = self._get_list()

    def _request(self):
        '''a helper methode that call the GET requests and return the reposnse if it was a success 
otherwise it raise an exception'''
        response =requests.get(self.url) 
        status = response.status_code
        if  (status == 200) or (status == 301):
            return response.json()
        elif status == 401:
            raise ApiError("Unauthorized access( Wrong API key? )")
        elif status == 400:
            raise ApiError("bad request")
        elif status == 403:
            raise ApiError("Access is forbidden, permission denied")
        elif status == 400:
            raise ApiError("Not found")
    

    
    def _get_list(self): 
        """helper method that make the request to the api """
        return self._request()["list"]
    
    def _get_data(self, data_name):
        """helper method that extact the data from the api response depending on it's name"""
        data_list = []
        dates_list = self._get_list()
        for i in range(len(dates_list)):
            date = dates_list[i]["dt_txt"]
            data_item = dates_list[i][data_name]
            data_list.append((date, data_item))
        return data_list
    
    def get_weathers(self):
        """this method uses the _get_data method to to exctract the weather releated data"""
        return self._get_data("weather")
        
    
    def get_winds(self):
        """this method uses the _get_data method to to exctract the wind releated data"""
        return self._get_data("wind")


    def get_temperature(self):
        """this method uses the _get_data method to to exctract the wind releated data"""
        return self._get_data("main")


    def get_all_data(self):
        """this method uses the _get_data method to to exctract the all releated data to the weather app"""
        #return None #unfinished 
        dates_lst = self._dates_lst
        
        
        result = []
        for i in range(len(dates_lst)):
            date_lst = dates_lst[i]["dt_txt"]
            temp_lst = self._get_data("main")[i][1]["temp"]
            weather_lst = self._get_data("weather")[i][1][0]["main"]
            weather_desc_lst = self._get_data("weather")[i][1][0]["description"]
            wind_speed_lst = self._get_data("wind")[i][1]["speed"] 
            wind_deg_lst = self._get_data("wind")[i][1]["deg"] 
            yield temp_lst, date_lst, weather_lst, weather_desc_lst, wind_speed_lst, wind_deg_lst
            #result.append((date_lst, weather_lst, weather_desc_lst, wind_speed_lst, wind_deg_lst))
        #return  result

    

    