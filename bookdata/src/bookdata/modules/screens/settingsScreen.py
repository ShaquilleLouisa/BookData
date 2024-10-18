from bookdata.modules.screens import *
from bookdata.modules.widgets import *

class SettingsScreen(Screen):
    def startup(self, refresh, save):
        screen, box = Screen.startup(self, "Settings")
        SettingsScreen.refresh = refresh
        SettingsScreen.save = save
        buttonOutline, SettingsScreen.button = Widgets.createButton(
            self,
            "Dark Theme",
            SettingsScreen.setDarkTheme,
            (0, 0, 0, 0),
            (0, 1, 0, 0),
        )
        box.add(buttonOutline)
        buttonOutline, SettingsScreen.button = Widgets.createButton(
            self,
            "White Theme",
            SettingsScreen.setWhiteTheme,
            (0, 0, 0, 0),
            (0, 1, 0, 0),
        )
        box.add(buttonOutline)
        return screen

    def setDarkTheme(self):
        Widgets.primaryColor = Widgets.darkThemePrimaryColor
        Widgets.secondaryColor = Widgets.darkThemeSecondaryColor
        SettingsScreen.updateTheme(self)

    def setWhiteTheme(self):
        Widgets.primaryColor = Widgets.lightThemePrimaryColor
        Widgets.secondaryColor = Widgets.lightThemeSecondaryColor
        SettingsScreen.updateTheme(self)
        
    def updateTheme(self):
        SettingsScreen.save()
        SettingsScreen.refresh()
