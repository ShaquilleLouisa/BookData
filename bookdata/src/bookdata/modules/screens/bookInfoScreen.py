from bookdata.modules.screens import *
from bookdata.modules.widgets import *

class BookInfoScreen(Screen):
    def startup(self, bookName):
        screen, box = Screen.startup(self, bookName)
        return screen