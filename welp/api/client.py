
import requests
from .google.geolocation import Geolocation

class Client:
    def __init__(self):
        self.session = requests.session()
        self.geolocation = Geolocation(self)