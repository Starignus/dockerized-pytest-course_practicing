"""
 For this example, we will define a module to create points that consist of a city name, its latitude and longitude coordinates.
"""


class Point():
    def __init__(self, name, latitude, longitude):
        # so they are not accessible to the user we use "_"
        self._name = name
        self._latitude = latitude
        self.longitude = longitude
   
    def get_lat_log(self):
        return self._latitude, self.longitude