import time
from features.pageobjects.Base import BaseSettingsPage


class Search(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def searchbox(self, search):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("searchbox_NAME",search)

    def clicksearch(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("searchbutton_XPATH")
        time.sleep(10)