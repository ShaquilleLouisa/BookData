import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

from toga.colors import WHITE
from toga.colors import BLACK

from toga.constants import Baseline
from toga.fonts import SANS_SERIF

from bookdata.modules.widgets import *

class StartScreen:
    startScreen = toga.Box()
    
    def startup(self):
        self.startScreen = toga.Box(style=Pack(direction=COLUMN, background_color=WHITE))
        self.startScreen.add(Widgets.createButton(
            self, "My Book List", 
            self.openAddBookScreen))
        return self.startScreen
