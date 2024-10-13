import toga
from toga.style import Pack

from bookdata.modules.screens.startScreen import *
from bookdata.modules.screens.statisticsScreen import *
from bookdata.modules.screens.settingsScreen import *
from bookdata.modules.widgets import *

class BookData(toga.App):
    def startup(self):
        BookData.mainBox = toga.Box(style=Pack(background_color=Widgets.primaryColor))
        BookData.mainBox.add(StartScreen.startup(self))
        self.main_window = toga.Window(title=self.formal_name, closable=True)
        self.main_window.content = self.mainBox
        self.main_window.show()
        
    def closeScreen():
        BookData.mainBox.remove(BookData.mainBox.children[0])
                
    def openStartScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.add(StartScreen.startup(self))
                    
    def openStatisticsScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.add(StatisticsScreen.startup(self, self.openStartScreen))
        
    def openSettingsScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.style.update(background_color=Widgets.primaryColor)
        BookData.mainBox.add(SettingsScreen.startup(self, self.openSettingsScreen))

def main():
    return BookData()
