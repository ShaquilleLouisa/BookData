"""
You can use this app to track the books you have read and compare your reading speed over time.
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class BookData(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return BookData()
