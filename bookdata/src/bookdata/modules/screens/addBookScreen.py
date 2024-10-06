from bookdata.modules.widgets import *

class AddBookScreen:
    addBookScreen = toga.Box()
    
    def startup(self):
        self.addBookScreen = toga.Box(style=Pack(direction=COLUMN, background_color=WHITE))
        topBox = toga.Box(style=Pack(padding_left=5,padding_right=5, direction=ROW,alignment=CENTER,background_color=WHITE))
        topBox.add(Widgets.createButton(self, "Back", self.openStartScreen,0, 0, (1, 0, 1, 1)))
        self.labelAndInput, AddBookScreen.bookInput = Widgets.createLabelAndInput(
            self, "Add book: "
        )
        topBox.add(self.labelAndInput)
        self.addBookScreen.add(topBox)
        self.addBookScreen.add(Widgets.createButton(self, "Add Book", AddBookScreen.addBook))
        AddBookScreen.books = Widgets.createBox(self, COLUMN)
        self.addBookScreen.add(AddBookScreen.books)
        return self.addBookScreen

    def addBook(self):
        bookName = AddBookScreen.bookInput.value.strip()
        if not bookName:
            return
        outline = toga.Box(style=Pack(direction=COLUMN, background_color=BLACK))
        box = toga.Box(
            style=Pack(
                direction=ROW, alignment=CENTER,background_color=WHITE,
                padding_top= 0 if len(AddBookScreen.books.children) > 0 else 1,
                padding_bottom=1,padding_left=1,padding_right=1
            )
        )
        bookLabel = Widgets.createLabel(self, bookName, 1)
        box.add(bookLabel)
        box.add(Widgets.createButton(
                self, "Remove Book", 
                lambda a : AddBookScreen.deleteBook(outline), 
                0, 0, (0, 0, 1, 0)
            ))
        outline.add(box)
        AddBookScreen.books.add(outline)
        AddBookScreen.bookInput.value = ""

    def deleteBook(box : toga.Box, **_: any):
        AddBookScreen.books.remove(box)
        AddBookScreen.setTopBorder()
        
    def setTopBorder():
        if len(AddBookScreen.books.children) > 0:
            AddBookScreen.books.children[0].children[0].style.update(padding_top= 1)