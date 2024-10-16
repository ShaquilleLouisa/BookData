import toga
from toga.colors import WHITE, BLACK, RED, BLUE
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

class Widgets:
    darkThemePrimaryColor = "#222222"
    darkThemeSecondaryColor = "#ffffff"

    lightThemePrimaryColor = "#ffffff"
    lightThemeSecondaryColor = "#000000"

    primaryColor = lightThemePrimaryColor
    secondaryColor = lightThemeSecondaryColor
    
    toggles = {}
    
    editingEnabled = False

    def createLabel(
        self, text, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1), flex=0, height=0
    ):
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
            text,
            style=Pack(
                padding=0,
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
                flex=flex,
                text_align=CENTER,
            ),
        )
        if height > 0:
            label.style.update(height=height)
            label.style.update(font_size=height / 2 + 2)
        box.add(label)
        outline.add(box)
        return outline

    def createButton(
        self, text, action, padding=(1, 1, 1, 1), borders=(1, 1, 1, 1), flex=0, height=0
    ):
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
            style=Pack(
                padding=0,
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
                flex=1,
            ),
        )
        if height > 0:
            self.button.style.update(height=height)
        box.add(self.button)
        outline.add(box)
        return outline, self.button

    def createToggle(self, text, enableAction, disableAction, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1)):
        toggle = Widgets.createButton(self, text, Widgets.toggle, padding, borders)
        Widgets.toggles[text] = (enableAction, disableAction)
        return toggle

    def toggle(self):
        if self.text != "Edit" and not Widgets.editingEnabled:
            return
        buttonColor = Widgets.fromRGB(self, self.style.background_color)
        parentColor = Widgets.fromRGB(self, self.parent.parent.style.background_color)
        
        def turnOn():
            Widgets.toggles[self.text][0]()
            self.style.update(background_color=Widgets.secondaryColor)
            self.style.update(color=Widgets.primaryColor)
        def turnOff():
            Widgets.toggles[self.text][1]()
            self.style.update(background_color=Widgets.primaryColor)
            self.style.update(color=Widgets.secondaryColor)
            
        if str(parentColor) == str(Widgets.lightThemeSecondaryColor):
            if str(buttonColor) == str(Widgets.lightThemePrimaryColor):
                turnOn()
            else:
                turnOff()
        elif str(parentColor) == str(Widgets.darkThemeSecondaryColor):
            if str(buttonColor) == str(Widgets.darkThemePrimaryColor):
                turnOn()
            else:
                turnOff()

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

    def fromRGB(self, rgb):
        res = str(rgb)[4:-1]
        res = tuple(map(int, res.split(", ")))
        return "#%02x%02x%02x" % res


class Screen:
    def startup(self, title, rightWidget=None):
        screen = toga.Box(
            style=Pack(
                direction=COLUMN,
                background_color=Widgets.primaryColor,
                flex=1,
                padding=5,
            )
        )
        boxOutline, box = Widgets.createBox(self, COLUMN, (0, 0, 0, 0), (1, 1, 1, 1), 1)
        screen.add(Screen.createScrollContainer(self, boxOutline))
        box.add(Screen.createTopBar(self, title, rightWidget))
        return screen, box

    def createTopBar(self, title, rightWidget=None):
        topBar = toga.Box(
            style=Pack(direction=ROW, background_color=Widgets.primaryColor)
        )
        topBar.add(
            Widgets.createButton(
                self, "Back", self.openStartScreen, (0, 0, 0, 0), (0, 1, 0, 1)
            )[0]
        )
        topBar.add(
            Widgets.createLabel(self, title, (0, 0, 0, 0), (0, 1, 0, 0), True, 48)
        )
        if rightWidget is not None:
            topBar.add(rightWidget)
        return topBar

    def createScrollContainer(self, boxOutline):
        scrollContainer = toga.ScrollContainer(
            content=boxOutline, on_scroll=self.openStartScreen
        )
        scrollContainer._MIN_HEIGHT = 768
        return scrollContainer
    
    # def createLabelAndInput(
    #     self, text, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1), flex=0, height=0
    # ):
    #     label = Widgets.createLabel(
    #         self, text, padding, (0, 1, 0, 1), flex, height=height
    #     )
    #     textInput = toga.TextInput(style=Pack(flex=1))
    #     outline, box = Widgets.createBox(self, ROW, padding, borders, flex)
    #     box.add(label)
    #     box.add(textInput)
    #     return outline, textInput

    # def createLabelAndButton(self, text, action):
    #     label = Widgets.createLabel(self, text)
    #     button = Widgets.createButton(self, text, action, 0, 0)
    #     outline, box = Widgets.createBox(self, COLUMN)
    #     box.add(label)
    #     box.add(button)
    #     return outline, button

    # def createEditableLabel(
    #     self, text, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1), flex=0, height=0
    # ):
    #     # label = Widgets.createLabel(self, text, padding, (0, 1, 0, 1), flex, height=height)
    #     textInput = toga.TextInput(style=Pack(flex=1), readonly=True)
    #     outline, box = Widgets.createBox(self, ROW, padding, borders, flex)
    #     box.add(textInput)
    #     textInput.value = text
    #     return outline, textInput
    
    # toggle = toga.Button()
    #     toggleAction = Widgets.toggle(toggle, enableAction, disableAction)
    #     outline, toggle = Widgets.createButton(self, text, lambda : toggleAction, padding, borders)
    #     return outline, toggle