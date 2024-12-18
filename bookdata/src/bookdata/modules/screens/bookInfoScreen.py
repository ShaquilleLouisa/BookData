import datetime
from bookdata.modules.screens.startScreen import *
from bookdata.modules.widgets import *


class BookInfoScreen(Screen):
    editableButtons = []
    statusOptions = ["Plan To Read", "Reading", "Read"]
    stars = ["★", "★", "★", "★", "★"]
    dates = ["startDate", "endDate"]

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
            (0, 0, 1, 0),
        )[0]
        screen, box = Screen.startup(self, bookName, editToggle)

        statusOptionsToggle = Widgets.createOptionsToggle(
            self, BookInfoScreen.statusOptions
        )
        dateInput, BookInfoScreen.dateInputs = Widgets.createStartEndDateInput(self)
        authorBox, BookInfoScreen.authorNameInput = Widgets.createLabelInput(self)
        pageBox, BookInfoScreen.pageInput = Widgets.createNumberInput(self)
        starsOptionsToggle = Widgets.createOptionsToggle(
            self, BookInfoScreen.stars, True
        )

        BookInfoScreen.editableButtons.append(
            [
                statusOptionsToggle,
                starsOptionsToggle,
                dateInput,
                authorBox,
                pageBox,
            ]
        )
        box.add(statusOptionsToggle, dateInput, authorBox, pageBox, starsOptionsToggle)

        BookInfoScreen.loadInfo(self)
        return screen

    def loadInfo(self):
        bookInfo = StartScreen.bookdata[BookInfoScreen.bookName]
        print(bookInfo)
        BookInfoScreen.loadStatus(self, bookInfo, str(BookInfoScreen.statusOptions))
        BookInfoScreen.loadWriterName(self, bookInfo, "authorName")
        BookInfoScreen.loadNumberOfPages(self, bookInfo, "pages")
        BookInfoScreen.loadStars(self, bookInfo, str(BookInfoScreen.stars))
        BookInfoScreen.loadDates(self, bookInfo)

    def loadStatus(self, bookInfo, groupKey):
        if "status" not in bookInfo:
            bookInfo["status"] = f"{BookInfoScreen.statusOptions[0]}0"
        loadedValue = bookInfo["status"]
        Widgets.optionToggleValues[groupKey] = loadedValue
        group = Widgets.optionToggles[groupKey]
        for index, key in enumerate(group):
            toggle = group[key]
            if str(index) == loadedValue[-1:]:
                print(f"load status: {str(index)}")
                toggle.style.update(background_color=Widgets.secondaryColor)
                toggle.style.update(color=Widgets.primaryColor)
            else:
                toggle.style.update(background_color=Widgets.primaryColor)
                toggle.style.update(color=Widgets.secondaryColor)

    def loadWriterName(self, bookInfo, key):
        if key not in bookInfo:
            bookInfo[key] = ""
        loadedValue = bookInfo[key]
        print(f"load authorName: {str(loadedValue)}")
        Widgets.labelInputValues[key] = loadedValue
        if loadedValue not in ["", "None"]:
            BookInfoScreen.authorNameInput = Widgets.setNumberInputText(
                BookInfoScreen.authorNameInput, loadedValue
            )
            print("loaded authorName")

    def loadNumberOfPages(self, bookInfo, key):
        if key not in bookInfo:
            bookInfo[key] = ""
        loadedValue = bookInfo[key]
        print(f"load numberInput: {str(loadedValue)}")
        Widgets.numberInputValues[key] = loadedValue
        if loadedValue not in ["0", "", "None"]:
            BookInfoScreen.pageInput = Widgets.setNumberInputText(
                BookInfoScreen.pageInput, f"{loadedValue} pages"
            )
            print("loaded number")

    def loadStars(self, bookInfo, groupKey):
        if "stars" not in bookInfo:
            bookInfo["stars"] = ""
        loadedValue = bookInfo["stars"]
        Widgets.optionToggleValues[groupKey] = loadedValue
        group = Widgets.optionToggles[groupKey]
        for index, key in enumerate(group):
            toggle = group[key]
            if str(index) == loadedValue[-1:]:
                print(f"load star: {str(index)}")
                toggle.style.update(background_color=Widgets.secondaryColor)
                toggle.style.update(color=Widgets.primaryColor)
            else:
                toggle.style.update(background_color=Widgets.primaryColor)
                toggle.style.update(color=Widgets.secondaryColor)

    def loadDates(self, bookInfo):
        for i in range(len(BookInfoScreen.dates)):
            if BookInfoScreen.dates[i] not in bookInfo:
                bookInfo[BookInfoScreen.dates[i]] = datetime.date.today()
            print(bookInfo[BookInfoScreen.dates[i]])
            loadedValue = bookInfo[BookInfoScreen.dates[i]]
            Widgets.dateInputValues[BookInfoScreen.dates[i]] = loadedValue
            Widgets.dateInputs[BookInfoScreen.dates[i]].value = loadedValue
            if loadedValue != "":
                BookInfoScreen.dateInputs[i] = Widgets.setDateInputText(
                    BookInfoScreen.dateInputs[i],
                    f"{loadedValue}",
                    BookInfoScreen.dates[i],
                )
        print("loaded loadDates")

    def onEnableClickEdit(self):
        Widgets.editingEnabled = True
        BookInfoScreen.pageInput = Widgets.setNumberInput(BookInfoScreen.pageInput)
        BookInfoScreen.enableEditPages(self)
        BookInfoScreen.enableEditAuthorName(self)
        BookInfoScreen.enableEditDates(self)

    def enableEditPages(self):
        if Widgets.numberInputValues["pages"] not in ["0", "", "None"]:
            BookInfoScreen.pageInput.value = int(Widgets.numberInputValues["pages"])

    def enableEditAuthorName(self):
        BookInfoScreen.authorNameInput = Widgets.setLabelInput(
            BookInfoScreen.authorNameInput
        )
        if Widgets.labelInputValues["authorName"] not in ["", "None"]:
            BookInfoScreen.authorNameInput.value = Widgets.labelInputValues[
                "authorName"
            ]

    def enableEditDates(self):
        for i in range(len(Widgets.dateInputValues)):
            BookInfoScreen.dateInputs[i] = Widgets.setDateInput(
                BookInfoScreen.dateInputs[i], BookInfoScreen.dates[i]
            )
            if Widgets.dateInputValues[BookInfoScreen.dates[i]] != "":
                BookInfoScreen.dateInputs[i].value = Widgets.dateInputValues[
                    BookInfoScreen.dates[i]
                ]

    def onDisableClickEdit(self):
        Widgets.editingEnabled = False
        BookInfoScreen.disableEditAuthorName(self)
        BookInfoScreen.disableEditPages(self)
        BookInfoScreen.disableEditDates(self)

    def disableEditAuthorName(self):
        value = Widgets.labelInputValues["authorName"]
        if value not in ["", "None"]:
            BookInfoScreen.authorNameInput = Widgets.setLabelInputText(
                BookInfoScreen.authorNameInput, value
            )
        else:
            BookInfoScreen.authorNameInput = Widgets.setLabelInputPlaceHolder(
                BookInfoScreen.authorNameInput
            )

    def disableEditPages(self):
        value = Widgets.numberInputValues["pages"]
        if value not in ["0", "", "None"]:
            BookInfoScreen.pageInput = Widgets.setNumberInputText(
                BookInfoScreen.pageInput, f"{value} pages"
            )
        else:
            BookInfoScreen.pageInput = Widgets.setNumberInputPlaceHolder(
                BookInfoScreen.pageInput
            )

    def disableEditDates(self):
        for i in range(len(Widgets.dateInputValues)):
            value = Widgets.dateInputValues[BookInfoScreen.dates[i]]
            BookInfoScreen.dateInputs[i] = Widgets.setDateInputText(
                BookInfoScreen.dateInputs[i], value, BookInfoScreen.dates[i]
            )

    def updateData(self):
        print("update book data")
        status = Widgets.optionToggleValues[str(BookInfoScreen.statusOptions)]
        bookData = StartScreen.bookdata[BookInfoScreen.bookName]
        bookData["status"] = status
        BookInfoScreen.updateStarData(self, status, bookData)
        bookData["authorName"] = Widgets.labelInputValues["authorName"]
        bookData["pages"] = Widgets.numberInputValues["pages"]
        bookData["startDate"] = Widgets.dateInputValues["startDate"]
        bookData["endDate"] = Widgets.dateInputValues["endDate"]
        BookInfoScreen.save()

    def updateStarData(self, status, bookData):
        starGroup = Widgets.optionToggles[str(BookInfoScreen.stars)]
        finished = BookInfoScreen.finished(self, status)
        for star in starGroup:
            starGroup[star].enabled = finished
        if finished:
            bookData["stars"] = Widgets.optionToggleValues[str(BookInfoScreen.stars)]
        else:
            bookData["stars"] = ""
            for key in starGroup:
                starGroup[key].style.update(background_color=Widgets.primaryColor)
                starGroup[key].style.update(color=Widgets.secondaryColor)

    def finished(self, status):
        return status == f"{str(BookInfoScreen.statusOptions[2])}2"
