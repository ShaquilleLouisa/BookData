from bookdata.modules.screens import *
from bookdata.modules.widgets import *
import json
import os.path

class SettingsScreen(Screen):
    def startup(self, refresh):
        screen, box = Screen.startup(self, "Settings")
        SettingsScreen.refresh = refresh
        buttonOutline, SettingsScreen.button = Widgets.createButton(
            self,
            "Dark Theme",
            SettingsScreen.setDarkTheme,
            (0, 0, 0, 0),
            (0, 1, 0, 0),
            0,
            50,
        )
        box.add(buttonOutline)
        buttonOutline, SettingsScreen.button = Widgets.createButton(
            self,
            "White Theme",
            SettingsScreen.setWhiteTheme,
            (0, 0, 0, 0),
            (0, 1, 0, 0),
            0,
            50,
        )
        box.add(buttonOutline)
        return screen

    def loadTheme(self, path):
        SettingsScreen.path = path
        if os.path.isfile(SettingsScreen.path):
            with open(SettingsScreen.path) as file:
                SettingsScreen.data = json.load(file)
                Widgets.primaryColor = SettingsScreen.data["primaryColor"]
                Widgets.secondaryColor = SettingsScreen.data["secondaryColor"]
                Widgets.textColor = SettingsScreen.data["textColor"]
        else:
            SettingsScreen.saveTheme(self)

    def saveTheme(self):
        SettingsScreen.data = {
            "primaryColor": Widgets.primaryColor,
            "secondaryColor": Widgets.secondaryColor,
            "textColor": Widgets.textColor,
        }
        with open(SettingsScreen.path, "w") as file:
            json.dump(SettingsScreen.data, file)

    def setDarkTheme(self):
        Widgets.primaryColor = "#222222"
        Widgets.secondaryColor = WHITE
        Widgets.textColor = WHITE
        SettingsScreen.updateTheme(self)

    def setWhiteTheme(self):
        Widgets.primaryColor = WHITE
        Widgets.secondaryColor = BLACK
        Widgets.textColor = BLACK
        SettingsScreen.updateTheme(self)
        
    def updateTheme(self):
        SettingsScreen.saveTheme(self)
        SettingsScreen.refresh()
