from bookdata.modules.screens import *
from bookdata.modules.widgets import *

class BookInfoScreen(Screen):
    editableButtons = []
    def startup(self, bookName):
        editToggle = Widgets.createToggle(
            self,
            "Edit",
            BookInfoScreen.onEnableClickEdit,
            BookInfoScreen.onDisableClickEdit,
            (0, 0, 0, 0),
            (0, 1, 1, 0),
        )[0]
        screen, box = Screen.startup(self, bookName, editToggle)
        
        outline, toggle = Widgets.createToggle(
                self,
                "Read",
                BookInfoScreen.onClickRead,
                BookInfoScreen.onClickNotRead,
                (0, 0, 0, 0),
                (0, 1, 0, 0),
            )
        box.add(outline)
        BookInfoScreen.editableButtons.append(toggle)
        
        return screen

    def onEnableClickEdit():
        Widgets.editingEnabled = True

    def onDisableClickEdit():
        Widgets.editingEnabled = False


    def onClickRead():
        pass
    def onClickNotRead():
        pass
