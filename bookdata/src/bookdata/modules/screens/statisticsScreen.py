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
                height=1000
            )
        ))
        return screen
    
    def restructureText(text):
        result = ""
        row = ""
        previousC = ""
        for c in str(text):
            row += c
            if c == "}" or previousC + c == ":{":
                result += "\n" + row 
                row = ""
            previousC = c
        return result