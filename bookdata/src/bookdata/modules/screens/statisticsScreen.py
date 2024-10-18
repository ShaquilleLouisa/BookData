from bookdata.modules.screens import *
from bookdata.modules.widgets import *


class StatisticsScreen(Screen):
    def startup(self, refresh):
        StatisticsScreen.refresh = refresh
        screen, box = Screen.startup(self, "Statistics")
        box.add(Widgets.createLabel(self, "hi", (0, 0, 0, 0), (0, 1, 0, 0), 0, 18))
        return screen
