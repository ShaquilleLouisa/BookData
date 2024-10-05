import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from toga.colors import WHITE
from toga.colors import BLACK

from toga.constants import Baseline
from toga.fonts import SANS_SERIF

class BookData(toga.App):
    def startup(self):
        self.mainBox = toga.Box(style=Pack(direction=COLUMN))
        self.createWidgets()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.mainBox
        self.main_window.show()
        
    def createWidgets(self):
        bookLabel = toga.Label(
            "Add book: ",
            style=Pack(padding=(0, 5))
        )
        self.bookInput = toga.TextInput(style=Pack(flex=1))
        
        self.createButton()
        
        bookBox = toga.Box(style=Pack(direction=ROW,padding=5))
        bookBox.add(bookLabel)
        bookBox.add(self.bookInput)
        
        self.books = toga.Box(style=Pack(direction=COLUMN, padding=5))
        self.mainBox.add(bookBox)
        self.mainBox.add(self.addBookButtonFrame)
        self.mainBox.add(self.books)
        
    def createButton(self):
        self.addBookButtonFrame = toga.Box(style=Pack(direction=COLUMN,padding_right=5,padding_left=5,background_color=BLACK))
        box = toga.Box(
            style=Pack(direction=COLUMN,padding=1,background_color=WHITE,color=BLACK)
        )
        addBookButton = toga.Button(
            "Add book",
            on_press=self.addBook,
            style=Pack(padding=0,background_color=WHITE)
        )
        box.add(addBookButton)
        self.addBookButtonFrame.add(box)
        
    def addBook(self, text):
        bookName=self.bookInput.value.strip()
        if not bookName:
            return
        bookLabel = toga.Label(bookName, style=Pack(padding=(0,5),flex=1))
        removeBookButton = toga.Button(
            "Remove Book",
            on_press=self.deleteBook,
            style=Pack(padding=0)
        )
        todo_box = toga.Box(style=Pack(direction=ROW,padding=5))
        todo_box.add(bookLabel)
        todo_box.add(removeBookButton)
        self.books.add(todo_box)
        self.bookInput.value=""
        
    def deleteBook(self, widget: toga.Button, **_: any):
        if widget.parent is None:
            return
        self.books.remove(widget.parent)


def main():
    return BookData()
