from bookdata.modules.screens import *
from bookdata.modules.widgets import *

class StatisticsScreen(Screen):
    def startup(self, refresh, bookData):
        StatisticsScreen.refresh = refresh
        screen, box = Screen.startup(self, "Statistics")
        box.add(toga.MultilineTextInput(
            value=StatisticsScreen.restructureText(bookData),
            style=Pack(
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
                height=500
            )
        ))
        return screen
    
    def restructureText(self):
        result = ""
        row = ""
        previousC = ""
        for c in str(self):
            row += c
            if c == "}" or previousC + c == ":{":
                result += row + "\n"
                row = ""
            previousC = c
        return result