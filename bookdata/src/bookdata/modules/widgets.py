import toga
from toga.colors import WHITE, BLACK
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

class Widgets:
    primaryColor = WHITE
    secondaryColor = BLACK
    textColor = BLACK
    
    def createLabel(self, text, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1), flex=0, height=0):
        outline = toga.Box(
            style=Pack(
                direction=COLUMN,
                padding_top=padding[0],
                padding_bottom=padding[1],
                padding_left=padding[2],
                padding_right=padding[3],
                background_color=Widgets.secondaryColor,
                flex=flex,
            )
        )
        box = toga.Box(
            style=Pack(
                direction=COLUMN,
                background_color=Widgets.primaryColor,
                flex=flex,
                padding_top=borders[0],
                padding_bottom=borders[1],
                padding_left=borders[2],
                padding_right=borders[3],
            )
        )
        label = toga.Label(
            text, style=Pack(padding=0, background_color=Widgets.primaryColor, color=Widgets.textColor, flex=flex, text_align=CENTER)
        )
        if height > 0:
            label.style.update(height=height)
            label.style.update(font_size=height/2+2)
        box.add(label)
        outline.add(box)
        return outline

    def createButton(
        self, text, action, padding=(1, 1, 1, 1), borders=(1, 1, 1, 1), flex=0, height=0):
        outline = toga.Box(
            style=Pack(
                direction=COLUMN,
                padding_top=padding[0],
                padding_bottom=padding[1],
                padding_left=padding[2],
                padding_right=padding[3],
                background_color=Widgets.secondaryColor,
                flex=flex,
            )
        )
        box = toga.Box(
            style=Pack(
                direction=COLUMN,
                background_color=Widgets.primaryColor,
                flex=1,
                padding_top=borders[0],
                padding_bottom=borders[1],
                padding_left=borders[2],
                padding_right=borders[3],
            )
        )
        self.button = toga.Button(
            text,
            on_press=action,
            style=Pack(padding=0, background_color=Widgets.primaryColor, color=Widgets.textColor, flex=1),
        )
        if height > 0:
            self.button.style.update(height=height)
        box.add(self.button)
        outline.add(box)
        return outline, self.button

    def createLabelAndInput(self, text, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1), flex=0, height=0):
        label = Widgets.createLabel(self, text, padding, (0, 1, 0, 1), flex, height=height)
        textInput = toga.TextInput(style=Pack(flex=1))
        outline, box = Widgets.createBox(self, ROW, padding, borders, flex)
        box.add(label)
        box.add(textInput)
        return outline, textInput

    def createLabelAndButton(self, text, action):
        label = Widgets.createLabel(self, text)
        button = Widgets.createButton(self, text, action, 0, 0)
        outline, box = Widgets.createBox(self, COLUMN)
        box.add(label)
        box.add(button)
        return outline, button

    def createBox(self, direction, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1), flex=0):
        outline = toga.Box(
            style=Pack(
                direction=COLUMN,
                padding_top=padding[0],
                padding_bottom=padding[1],
                padding_left=padding[2],
                padding_right=padding[3],
                background_color=Widgets.secondaryColor,
                flex=flex,
            )
        )
        box = toga.Box(
            style=Pack(
                direction=direction,
                background_color=Widgets.primaryColor,
                flex=1,
                padding_top=borders[0],
                padding_bottom=borders[1],
                padding_left=borders[2],
                padding_right=borders[3],
            )
        )
        
        outline.add(box)
        return outline, box
        
class Screen:
    def startup(self, title):
        screen = toga.Box(style=Pack(direction=COLUMN, background_color=Widgets.primaryColor, flex = 1, padding=5))
        boxOutline, box = Widgets.createBox(self, COLUMN, (0,0,0,0), (1,1,1,1), 1)
        screen.add(Screen.createScrollContainer(self, boxOutline))
        box.add(Screen.createTopBar(self, title))
        return screen, box
    
    def createTopBar(self, title):
        topBar = toga.Box(style=Pack(direction=ROW, background_color=Widgets.primaryColor))
        topBar.add(Widgets.createButton(
            self, "Back", 
            self.openStartScreen,
            (0,0,0,0), (0,1,0,1))[0])
        topBar.add(Widgets.createLabel(self, title, (0,0,0,0), (0,1,0,0), True, 48))
        return topBar
    
    def createScrollContainer(self, boxOutline):
        scrollContainer = toga.ScrollContainer(content=boxOutline ,on_scroll=self.openStartScreen)
        scrollContainer._MIN_HEIGHT = 790
        return scrollContainer

