import json
import os
import sys
import toga
from toga.style import Pack

from bookdata.modules.screens.startScreen import *
from bookdata.modules.screens.statisticsScreen import *
from bookdata.modules.screens.settingsScreen import *
from bookdata.modules.screens.bookInfoScreen import *
from bookdata.modules.widgets import *

class BookData(toga.App):
    def startup(self):
        print("something 1")
        BookData.mainBox = toga.Box(style=Pack(background_color=Widgets.primaryColor))
        print("something 2")
        BookData.loadData(self)
        print("something 3")
        BookData.mainBox.add(
            StartScreen.startup(self, self.openBookInfoScreen, self.save)
        )
        self.main_window = toga.Window(title=self.formal_name, closable=True)
        self.main_window.content = self.mainBox
        self.main_window.show()
        
    def loadData(self):
        BookData.dataPath = f"{self.paths.data}\mydata.json"
        if sys.platform == "win32":
            print("testing on pc")
            StartScreen.bookdata = {}
            return
        if not os.path.isfile(BookData.dataPath):
            print("save not found")
            self.save()
        self.load()

    def load(self):
        print("something 2.1")
        f = open(BookData.dataPath, "r", encoding= 'utf-8')
        print(f.read())
        with open(BookData.dataPath, 'r', encoding= 'utf-8') as file:
            print("something 2.2")
            data = json.load(file)
            print("something 2.3")
            Widgets.primaryColor = data["settings"]["primaryColor"]
            Widgets.secondaryColor = data["settings"]["secondaryColor"]
            StartScreen.bookdata = data["books"]
        BookData.mainBox.style.update(background_color=Widgets.primaryColor)

    def saveData(self):
        print("update save")
        if sys.platform == "win32":
            print("testing on pc")
            return
        self.save()

    def save(self):
        if sys.platform == "win32":
            print("testing on pc")
            return
        print("new save")
        if dataIsDefaultData():
            data = App.getTemplate()
        else:
            data = {
                "settings": {
                    "primaryColor": Widgets.primaryColor,
                    "secondaryColor": Widgets.secondaryColor,
                },
                "books": StartScreen.bookdata,
            }
        with open(BookData.dataPath, "w") as file:
            json.dump(data, file)
    def dataIsDefaultData():
        return str(StartScreen.bookdata) == "{}" and Widgets.primaryColor == "#ffffff" and Widgets.primaryColor == "#000000"

    def closeScreen():
        Widgets.editingEnabled = False
        BookData.mainBox.remove(BookData.mainBox.children[0])

    def openStartScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.add(
            StartScreen.startup(self, self.openBookInfoScreen, self.saveData)
        )

    def openBookInfoScreen(self, bookName):
        BookData.closeScreen()
        BookData.mainBox.add(BookInfoScreen.startup(self, bookName, self.saveData))

    def openStatisticsScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.add(StatisticsScreen.startup(self, self.openStartScreen, StartScreen.bookdata))

    def openSettingsScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.style.update(background_color=Widgets.primaryColor)
        BookData.mainBox.add(
            SettingsScreen.startup(self, self.openSettingsScreen, self.saveData)
        )


def main():
    return BookData()

def getTemplate():
    return {
        "settings": {
                "primaryColor": "#ffffff",
                "secondaryColor": "#000000",
            },
            "books": "{}"
            }

