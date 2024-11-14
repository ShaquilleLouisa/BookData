import sys
import toga
from toga.colors import WHITE, BLACK, RED, BLUE
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, BOTTOM


class Widgets:
    darkThemePrimaryColor = "#222222"
    darkThemeSecondaryColor = "#ffffff"

    lightThemePrimaryColor = "#ffffff"
    lightThemeSecondaryColor = "#000000"

    primaryColor = lightThemePrimaryColor
    secondaryColor = lightThemeSecondaryColor

    toggles = {}
    optionToggles = {}
    optionToggleValues = {}
    optionTogglecanDisable = {}
    numberInputs = {}
    numberInputValues = {}
    labelInputs = {}
    labelInputValues = {}
    dateInputs = {}
    dateInputValues = {}

    editingEnabled = False

    currentlyMaking = ""

    widgetCount = 0

    updateData = lambda: ()

    def createScrollContainer(self):
        box = toga.Box(style=Pack(direction=COLUMN))
        return box, toga.ScrollContainer(
            content=box,
            horizontal=True,
            vertical=True,
            style=Pack(direction=COLUMN, flex=1),
        )

    def createLabel(self, text):
        return toga.Label(
            text=text,
            style=Pack(
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
                font_size=15,
                height=40,
                padding_top=8,
                padding_left=12,
            ),
        )

    def createBoxedLabel(
        self, text, padding=(0, 0, 0, 0), borders=(1, 1, 1, 1), flex=0, height=0, width=0
    ):
        height = height // 2
        outline, box = Widgets.createBox(self, COLUMN, padding, borders, flex)

        labels = []
        if len(text) > 10:
            for i in range(2):
                labels.append(
                    toga.Label(
                        (text[: len(text) // 2] if i == 0 else text[len(text) // 2 :]),
                        style=Pack(
                            background_color=Widgets.primaryColor,
                            color=Widgets.secondaryColor,
                            flex=1,
                            text_align=CENTER
                        ),
                    )
                )
                box.add(labels[i])
        else:
            labels.append(
                toga.Label(
                    text,
                    style=Pack(
                        background_color=Widgets.primaryColor,
                        color=Widgets.secondaryColor,
                        flex=1,
                        text_align=CENTER
                    )
                )
            )
            box.add(labels[0])
        if height > 0:
            # if len(labels) > 1:
            #     fontSize = max(1, height - (len(text) // 1.1))
            # else:
            fontSize = max(1, height - (len(text) // 1.1))
            
            for label in labels:
                label.style.update(font_size=fontSize)
                label.style.update(text_align=CENTER)
        outline.add(box)
        if width > 0:
            for label in labels:
                label.style.update(width=width)
        outline.add(box)
        return outline

    def createLabelInput(self, padding=(0, 0, 0, 0), borders=(0, 1, 0, 0)):
        outline, box = Widgets.createBox(self, COLUMN, padding, borders)
        label = Widgets.createLabel(self, "Author's name")
        box.add(label)
        return outline, label

    def setLabelInputValue(self):
        if Widgets.editingEnabled:
            Widgets.labelInputValues["authorName"] = str(self.value)
            Widgets.updateData(self)

    def setLabelInputText(self, text):
        parent = self.parent
        parent.remove(self)
        label = Widgets.createLabel(self, text)
        parent.add(label)
        Widgets.labelInputs["authorName"] = label
        return label

    def setLabelInput(self):
        parent = self.parent
        parent.remove(self)
        labelInput = toga.TextInput(
            on_change=Widgets.setLabelInputValue,
            style=Pack(
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
            ),
        )
        parent.add(labelInput)
        Widgets.labelInputs["authorName"] = labelInput
        return labelInput

    def setLabelInputPlaceHolder(self):
        parent = self.parent
        parent.remove(self)
        label = Widgets.createLabel(self, "Author's name")
        parent.add(label)
        return label

    def createDateInput(self, action):
        return toga.DateInput(
            on_change=action,
            style=Pack(
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
                width=135,
            ),
        )

    def createStartEndDateInput(self, padding=(0, 0, 0, 0), borders=(0, 1, 0, 0)):
        outline, box = Widgets.createBox(self, ROW, padding, borders)
        startDate = Widgets.createDateInput(self, Widgets.setStartDateInputValue)
        Widgets.dateInputs["startDate"] = startDate
        endDate = Widgets.createDateInput(self, Widgets.setEndDateInputValue)
        Widgets.dateInputs["endDate"] = endDate
        box.add(startDate, toga.Box(self, style=Pack(flex=1)), endDate)
        return outline, [startDate, endDate]

    def setStartDateInputValue(self):
        if Widgets.editingEnabled:
            Widgets.dateInputValues["startDate"] = str(self.value)
            Widgets.updateData(self)

    def setEndDateInputValue(self):
        if Widgets.editingEnabled:
            Widgets.dateInputValues["endDate"] = str(self.value)
            Widgets.updateData(self)

    def setDateInputText(self, text, key):
        parent = self.parent
        parent.remove(self)
        label = Widgets.createLabel(self, f"{key[:-4]}: {text}  ")
        pos = 0 if key == "startDate" else 2
        parent.insert(pos, label)
        Widgets.dateInputs[key] = label
        return label

    def setDateInput(self, key):
        parent = self.parent
        parent.remove(self)
        if key == "startDate":
            startDate = Widgets.createDateInput(self, Widgets.setStartDateInputValue)
            Widgets.dateInputs["startDate"] = startDate
            parent.insert(0, startDate)
            return startDate
        elif key == "endDate":
            endDate = Widgets.createDateInput(self, Widgets.setEndDateInputValue)
            Widgets.dateInputs["endDate"] = endDate
            parent.insert(2, endDate)
            return endDate

    def createNumberInput(self, padding=(0, 0, 0, 0), borders=(0, 1, 0, 0)):
        outline, box = Widgets.createBox(self, COLUMN, padding, borders)
        label = Widgets.createLabel(self, "Number of pages")
        box.add(label)
        return outline, label

    def setNumberInputPlaceHolder(self):
        parent = self.parent
        parent.remove(self)
        label = Widgets.createLabel(self, "Number of pages")
        parent.add(label)
        return label

    def setNumberInput(self):
        parent = self.parent
        parent.remove(self)
        numberInput = toga.NumberInput(
            on_change=Widgets.setNumberInputValue,
            style=Pack(
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
            ),
        )
        pos = len(parent.children) - 1
        parent.insert(pos, numberInput)
        Widgets.numberInputs["pages"] = numberInput
        return numberInput

    def setNumberInputText(self, text):
        parent = self.parent
        parent.remove(self)
        numberInput = Widgets.createLabel(self, text)
        pos = len(parent.children) - 1
        parent.insert(pos, numberInput)
        Widgets.numberInputs["pages"] = numberInput
        return numberInput

    def setNumberInputValue(self):
        Widgets.numberInputValues["pages"] = str(self.value)
        Widgets.updateData(self)

    def createButton(
        self,
        text,
        action,
        padding=(1, 1, 1, 1),
        borders=(1, 1, 1, 1),
        flex=0,
        groupName="",
        height=0,
        id=0,
        width=0,
    ):
        outline, box = Widgets.createBox(self, COLUMN, padding, borders, flex)
        Widgets.widgetCount += 1
        button = toga.Button(
            id=(
                groupName + str(id)
                if groupName != ""
                else f"button{Widgets.widgetCount}"
            ),
            text=text,
            on_press=action,
            style=Pack(
                padding=0,
                background_color=Widgets.primaryColor,
                color=Widgets.secondaryColor,
                flex=1,
            ),
        )
        if height > 0:
            button.style.update(height=height)

        if width > 0:
            button.style.update(width=width)

        if len(text) > 33:
            button.style.update(font_size=10 - (len(text) - 34))

        box.add(button)
        outline.add(box)
        return outline, button

    def createOptionsToggle(
        self, texts, canDisable=False, padding=(0, 0, 0, 0), borders=(0, 1, 0, 0)
    ):
        groupName = str(texts)
        outline, box = Widgets.createBox(self, ROW, padding, borders)
        if groupName not in Widgets.optionToggles:
            Widgets.optionToggles[groupName] = {}
            Widgets.optionToggleValues[groupName] = ""
        for i in range(len(texts)):
            toggle = Widgets.createToggle(
                self,
                texts[i],
                Widgets.setOptionsToggleValue,
                Widgets.disableOptionsToggle if canDisable else None,
                (0, 0, 0, 0),
                (1, 1, 1, 1),
                1,
                groupName,
                i,
            )[1]
            Widgets.optionToggles[groupName][texts[i] + str(i)] = toggle
            width = 381 / len(texts)
            if width % 2 != 1 and i == len(texts) - 1:
                width += 1
            toggle.style.update(width=width)
            box.add(toggle)
        return outline

    def setOptionsToggleValue(self):
        groupKey = self.id[:-1]
        for index, key in enumerate(Widgets.optionToggles[groupKey]):
            if str(index) == self.id[-1:]:
                Widgets.optionToggleValues[groupKey] = key
            else:
                Widgets.optionToggles[groupKey][key].style.update(
                    background_color=Widgets.primaryColor
                )
                Widgets.optionToggles[groupKey][key].style.update(
                    color=Widgets.secondaryColor
                )
        Widgets.updateData(self)

    def disableOptionsToggle(self):
        groupKey = self.id[:-1]
        Widgets.optionToggleValues[groupKey] = ""
        Widgets.updateData(self)

    def createToggle(
        self,
        text,
        enableAction,
        disableAction,
        padding=(0, 0, 0, 0),
        borders=(1, 1, 1, 1),
        flex=0,
        groupName="",
        id=0,
    ):
        outline, button = Widgets.createButton(
            self, text, Widgets.toggle, padding, borders, flex, groupName, 0, id
        )
        Widgets.toggles[text] = (enableAction, disableAction)
        return outline, button

    def toggle(self):
        if self.text != "Edit" and not Widgets.editingEnabled:
            return
        buttonColor = Widgets.fromRGB(self, self.style.background_color)
        parentColor = Widgets.fromRGB(self, self.parent.parent.style.background_color)

        def turnOn():
            if self.text in Widgets.toggles:
                Widgets.toggles[self.text][0](self)
            self.style.update(background_color=Widgets.secondaryColor)
            self.style.update(color=Widgets.primaryColor)

        def turnOff():
            if self.text in Widgets.toggles and Widgets.toggles[self.text][1] != None:
                Widgets.toggles[self.text][1](self)
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
        Widgets.widgetCount += 1
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
                padding_top=borders[0],
                padding_bottom=borders[1],
                padding_left=borders[2],
                padding_right=borders[3],
                flex=1,
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
        topBar, box = Widgets.createBox(self, ROW, (0, 0, 0, 0), (0, 1, 0, 0))
        box.add(
            Widgets.createButton(
                self, "Back", self.openStartScreen, (0, 0, 0, 0), (0, 0, 0, 1)
            )[0]
        )
        titleBox = Widgets.createBoxedLabel(
            self, title, (0, 0, 0, 0), (0, 0, 0, 0), True, 48, 200
        )
        box.add(titleBox)

        if rightWidget is not None:
            box.add(rightWidget)
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
