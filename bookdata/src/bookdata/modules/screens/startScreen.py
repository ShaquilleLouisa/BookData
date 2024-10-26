from bookdata.modules.widgets import *


class StartScreen:
    bookdata = {}

    def startup(self, openBookInfoScreen, save):
        StartScreen.openBookInfoScreen = openBookInfoScreen
        StartScreen.save = save
        startScreen = toga.Box(
            style=Pack(
                background_color=Widgets.primaryColor,
                flex=1,
                padding=5,
                padding_bottom=0,
            )
        )
        outline, box = Widgets.createBox(self, COLUMN, (0, 0, 0, 0), (1, 1, 1, 1), 1)
        box.add(StartScreen.createTopBar(self, "Books"))
        StartScreen.bookInput = toga.TextInput(
            value="Book name",
            on_gain_focus=StartScreen.clearInput,
            style=Pack(
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
                flex=1,
            ),
        )
        box.add(StartScreen.bookInput)
        buttons = toga.Box(style=Pack(direction=ROW, flex=0))
        buttons.add(
            Widgets.createButton(
                self, "Add", StartScreen.onClickAddBook, (0, 0, 0, 0), (1, 1, 0, 1), 1
            )[0]
        )
        buttons.add(
            Widgets.createButton(
                self,
                "Search",
                StartScreen.onClickSearchBook,
                (0, 0, 0, 0),
                (1, 1, 0, 0),
                1,
            )[0]
        )
        box.add(StartScreen.bookInput)
        box.add(buttons)
        # StartScreen.books = Widgets.createBox(self, COLUMN, (0,0,0,0), (0,0,0,0))[0]
        StartScreen.books, scroll = Widgets.createScrollContainer(
            self
        )  # Widgets.createBox(self, COLUMN, (0,0,0,0), (0,0,0,0))[0]
        box.add(scroll)
        StartScreen.loadBooks(self)
        startScreen.add(outline)
        return startScreen

    def loadBooks(self):
        for value in StartScreen.bookdata:
            StartScreen.addBook(self, value)

    def clearInput(self):
        StartScreen.bookInput.value = ""

    def createTopBar(self, title):
        topBar, box = Widgets.createBox(self, ROW, (0, 0, 0, 0), (0, 1, 0, 0))
        box.add(
            Widgets.createButton(
                self, "Stat", self.openStatisticsScreen, (0, 0, 0, 0), (0, 0, 0, 1)
            )[0]
        )
        box.add(
            Widgets.createBoxedLabel(self, title, (0, 0, 0, 0), (0, 0, 0, 0), True, 48)
        )
        box.add(
            Widgets.createButton(
                self, "Set", self.openSettingsScreen, (0, 0, 0, 0), (0, 0, 1, 0)
            )[0]
        )
        return topBar
    
    def onClickSearchBook(self):
        StartScreen.books.clear()
        inputName = StartScreen.bookInput.value.strip()
        if not inputName or inputName == "Book name":
            StartScreen.loadBooks(self)
            return
        for book in StartScreen.bookdata:
            if book in inputName:
                StartScreen.addBook(self, book)

    def onClickAddBook(self):
        inputName = StartScreen.bookInput.value.strip()
        if not inputName or inputName == "Book name":
            return
        StartScreen.clearInput(self)
        StartScreen.bookdata[inputName] = {}
        StartScreen.save()
        StartScreen.addBook(self, inputName)

    def addBook(self, bookName):
        outline = toga.Box(
            style=Pack(direction=COLUMN, background_color=Widgets.secondaryColor)
        )
        box = toga.Box(
            style=Pack(
                direction=ROW,
                alignment=CENTER,
                background_color=Widgets.primaryColor,
                padding_top=0 if len(StartScreen.books.children) > 0 else 1,
                padding_bottom=1,
            )
        )
        box.add(
            Widgets.createButton(
                self,
                bookName,
                StartScreen.openBook,
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                1,
                "",
                0,
                0,
                290,
            )[0]
        )
        box.add(
            Widgets.createButton(
                self, "Remove", StartScreen.deleteBook, (0, 0, 0, 0), (0, 0, 1, 0)
            )[0]
        )
        outline.add(box)
        StartScreen.books.add(outline)

    def deleteBook(self, **_: any):
        StartScreen.books.remove(self.parent.parent.parent.parent)
        bookName = (
            self.parent.parent.parent.parent.children[0]
            .children[0]
            .children[0]
            .children[0]
            .text
        )
        print(bookName)
        if bookName in StartScreen.bookdata:
            StartScreen.bookdata.pop(bookName)
        StartScreen.save()

    def openBook(self):
        StartScreen.openBookInfoScreen(self.parent.children[0].text)
