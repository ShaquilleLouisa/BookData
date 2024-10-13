from bookdata.modules.screens import *
from bookdata.modules.widgets import *

class SettingsScreen(Screen):
    def startup(self, refresh):
        SettingsScreen.refresh = refresh
        screen, box = Screen.startup(self, "Settings")
        buttonOutline, SettingsScreen.button = Widgets.createButton(self, "Dark Theme", SettingsScreen.setDarkTheme, (0,0,0,0), (0,1,0,0), 0, 50)
        box.add(buttonOutline)
        buttonOutline, SettingsScreen.button = Widgets.createButton(self, "White Theme", SettingsScreen.setWhiteTheme, (0,0,0,0), (0,1,0,0), 0, 50)
        box.add(buttonOutline)
        return screen
    
    def setDarkTheme(self):
        print("setDarkTheme")
        Widgets.primaryColor = "#222222"
        Widgets.secondaryColor = WHITE
        Widgets.textColor = WHITE
        SettingsScreen.refresh()
        
    def setWhiteTheme(self):
        print("setWhiteTheme")
        Widgets.primaryColor = WHITE
        Widgets.secondaryColor = BLACK
        Widgets.textColor = BLACK
        SettingsScreen.refresh()
        
        
        
    
