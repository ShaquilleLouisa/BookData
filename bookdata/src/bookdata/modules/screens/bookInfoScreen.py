from bookdata.modules.screens.startScreen import *
from bookdata.modules.widgets import *

class BookInfoScreen(Screen):
    editableButtons = []
    statusOptions = ["Plan To Read", "Reading", "Read"]

    def startup(self, bookName, save):
        Widgets.updateData = BookInfoScreen.updateData
        BookInfoScreen.save = save
        BookInfoScreen.bookName = bookName
        editToggle = Widgets.createToggle(
            self,
            "Edit",
            BookInfoScreen.onEnableClickEdit,
            BookInfoScreen.onDisableClickEdit,
            (0, 0, 0, 0),
            (0, 1, 1, 0),
        )[0]
        screen, box = Screen.startup(self, bookName, editToggle)

        outline = Widgets.createOptionsToggle(
            self, BookInfoScreen.statusOptions, (0, 0, 0, 0), (0, 1, 0, 0)
        )
        BookInfoScreen.editableButtons.append(outline)
        box.add(outline)
        BookInfoScreen.loadInfo()
        return screen

    def loadInfo():
        groupKey = str(BookInfoScreen.statusOptions)
        loadedValue = StartScreen.bookdata[BookInfoScreen.bookName]["status"]
        Widgets.optionToggleValue[groupKey] = loadedValue
        group = Widgets.optionToggles[groupKey]
        for key in group:
            toggle = group[key]
            if toggle.text == loadedValue:
                toggle.style.update(background_color=Widgets.secondaryColor)
                toggle.style.update(color=Widgets.primaryColor)
            else:
                toggle.style.update(background_color=Widgets.primaryColor)
                toggle.style.update(color=Widgets.secondaryColor)

    def onEnableClickEdit(self):
        Widgets.editingEnabled = True

    def onDisableClickEdit(self):
        Widgets.editingEnabled = False

    def updateData(self):
        groupKey = str(BookInfoScreen.statusOptions)
        StartScreen.bookdata[BookInfoScreen.bookName]["status"] = (
            Widgets.optionToggleValue[groupKey]
        )
        BookInfoScreen.save
