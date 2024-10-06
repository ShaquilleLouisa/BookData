import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

from toga.colors import WHITE
from toga.colors import BLACK

from toga.constants import Baseline
from toga.fonts import SANS_SERIF

from bookdata.modules.screens.startScreen import *
from bookdata.modules.screens.addBookScreen import *

class BookData(toga.App):
    
    def startup(self):
        self.mainBox = toga.Box(style=Pack(direction=COLUMN, background_color=WHITE))
        self.mainBox.add(StartScreen.startup(self))
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.mainBox
        self.main_window.show()
        
    def openAddBookScreen(self, *_: any):
        self.mainBox.add(AddBookScreen.startup(self))
        self.mainBox.remove(self.mainBox.children[0])
        
    def openStartScreen(self, *_: any):
        self.mainBox.add(StartScreen.startup(self))
        self.mainBox.remove(self.mainBox.children[0])

def main():
    return BookData()
