from .menus import CursesWindow
from .api.client import Client


class Welp:
    def __init__(self):
        self.api_client = Client()
        self.ui = CursesWindow(self.api_client)
