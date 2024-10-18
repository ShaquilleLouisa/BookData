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
        BookData.mainBox = toga.Box(style=Pack(background_color=Widgets.primaryColor))
        BookData.loadData(self)
        BookData.mainBox.add(
            StartScreen.startup(self, self.openBookInfoScreen, self.saveData)
        )
        self.main_window = toga.Window(title=self.formal_name, closable=True)
        self.main_window.content = self.mainBox
        self.main_window.show()

    def loadData(self):
        self.dataPath = f"{self.paths.data}\mydata.json"
        if sys.platform == "win32":
            print("testing on pc")
            StartScreen.bookdata = {}
            return
        if not os.path.isfile(self.dataPath):
            print("save not found")
            self.save()
        self.load()

    def load(self):
        with open(self.dataPath) as file:
            data = json.load(file)
            Widgets.primaryColor = data["settings"]["primaryColor"]
            Widgets.secondaryColor = data["settings"]["secondaryColor"]
            Widgets.textColor = data["settings"]["textColor"]
            StartScreen.bookdata = data["books"]
        BookData.mainBox.style.update(background_color=Widgets.primaryColor)

    def saveData(self):
        print("update save")
        if sys.platform == "win32":
            print("testing on pc")
            return
        self.save()

    def save(self):
        print("new save")
        data = {
            "settings": {
                "primaryColor": Widgets.primaryColor,
                "secondaryColor": Widgets.secondaryColor,
                "textColor": Widgets.textColor,
            },
            "books": StartScreen.bookdata,
        }
        with open(self.dataPath, "w") as file:
            json.dump(data, file)

    def closeScreen():
        BookData.mainBox.remove(BookData.mainBox.children[0])

    def openStartScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.add(
            StartScreen.startup(self, self.openBookInfoScreen, self.saveData)
        )

    def openBookInfoScreen(self, bookName):
        BookData.closeScreen()
        BookData.mainBox.add(BookInfoScreen.startup(self, bookName))

    def openStatisticsScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.add(StatisticsScreen.startup(self, self.openStartScreen))

    def openSettingsScreen(self, *_: any):
        BookData.closeScreen()
        BookData.mainBox.style.update(background_color=Widgets.primaryColor)
        BookData.mainBox.add(
            SettingsScreen.startup(self, self.openSettingsScreen, self.saveData)
        )


def main():
    return BookData()
