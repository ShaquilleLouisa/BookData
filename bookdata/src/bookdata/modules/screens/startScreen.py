from bookdata.modules.widgets import *

class StartScreen:
    def startup(self):
        startScreen = toga.Box(style=Pack(background_color=Widgets.primaryColor, flex = 1, padding=5))
        outline, box = Widgets.createBox(self, COLUMN, (0,0,0,0), (1,1,1,1), 1)
        box.add(StartScreen.createTopBar(self, "Books"))
        StartScreen.bookInput = toga.TextInput(value="Book name", on_gain_focus= StartScreen.clearInput,
                                               style=Pack(background_color=Widgets.primaryColor,color=Widgets.textColor, flex=1))
        box.add(StartScreen.bookInput)
        buttons = toga.Box(style=Pack(direction=ROW, flex = 0))
        buttons.add(Widgets.createButton(self, "Add", StartScreen.addBook, (0,0,0,0), (1,1,0,1), 1)[0])
        buttons.add(Widgets.createButton(self, "Search", StartScreen.addBook, (0,0,0,0), (1,1,0,0), 1)[0])
        box.add(StartScreen.bookInput)
        box.add(buttons)
        StartScreen.books = Widgets.createBox(self, COLUMN, (0,0,0,0), (0,0,0,0))[0]
        box.add(StartScreen.books)
        startScreen.add(outline)
        return startScreen
    
    def clearInput(self):
        StartScreen.bookInput.value=""
    
    def createTopBar(self, title):
        topBar = toga.Box(style=Pack(direction=ROW, background_color=Widgets.primaryColor))
        topBar.add(Widgets.createButton(
            self, "Stat", 
            self.openStatisticsScreen,
            (0,0,0,0), (0,1,0,1))[0])
        topBar.add(Widgets.createLabel(self, title, (0,0,0,0), (0,1,0,0), True, 48))
        topBar.add(Widgets.createButton(
            self, "Set", 
            self.openSettingsScreen,
            (0,0,0,0), (0,1,1,0))[0])
        return topBar

    def addBook(self):
        bookName = StartScreen.bookInput.value.strip()
        StartScreen.clearInput(self)
        if not bookName:
            return
        outline = toga.Box(style=Pack(direction=COLUMN, background_color=Widgets.secondaryColor))
        box = toga.Box(
            style=Pack(
                direction=ROW, alignment=CENTER,background_color=Widgets.primaryColor,
                padding_top= 0 if len(StartScreen.books.children) > 0 else 1,
                padding_bottom=1
            )
        )
        box.add(Widgets.createLabel(self, bookName, (0,0,0,0), (0,0,0,0), 1))
        box.add(Widgets.createButton(self, "Remove", StartScreen.deleteBook, (0,0,0,0), (0, 0, 1, 0))[0])
        outline.add(box)
        StartScreen.books.add(outline)

    def deleteBook(self, **_: any):
        StartScreen.books.remove(self.parent.parent.parent.parent)
 
    
    