from .menus import CursesWindow
from .api.client import Client


class Welp:
    def __init__(self):
        self.ui = CursesWindow()
        self.api_client = Client()

        