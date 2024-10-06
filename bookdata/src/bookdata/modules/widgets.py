import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

from toga.colors import WHITE
from toga.colors import BLACK
from toga.colors import RED

from toga.constants import Baseline
from toga.fonts import SANS_SERIF


class Widgets:
    def createLabel(self, text, flex=0):
        return toga.Label(
            text,
            style=Pack(padding=0, flex=flex, background_color=WHITE, color=BLACK),
        )

    def createButton(self, text, action, padding_right=5, padding_left=5, borders=(1,1,1,1)):
        outline = toga.Box(
            style=Pack(
                direction=COLUMN,
                padding_right=padding_right,
                padding_left=padding_left,
                background_color=BLACK,
            )
        )
        box = toga.Box(style=Pack(direction=COLUMN, background_color=WHITE,
                                  padding_top=borders[0],padding_bottom=borders[1],
                                  padding_left=borders[2],padding_right=borders[3]))
        button = toga.Button(
            text,
            on_press=action,
            style=Pack(padding=0, background_color=WHITE, color=BLACK),
        )
        box.add(button)
        outline.add(box)
        return outline

    def createLabelAndInput(self, text):
        label = Widgets.createLabel(self, text)
        textInput = toga.TextInput(style=Pack(flex=1))
        box = Widgets.createBox(self, ROW, 0)
        box.add(label)
        box.add(textInput)
        return box, textInput

    def createLabelAndButton(self, text, action):
        label = Widgets.createLabel(self, text)
        button = Widgets.createButton(self, text, action, 0, 0)
        box = Widgets.createBox(self, ROW)
        box.add(label)
        box.add(button)
        return box, button

    def createBox(self, direction, padding = 5):
        return toga.Box(style=Pack(direction=direction,alignment=CENTER, padding=padding, background_color=WHITE, flex=1))
