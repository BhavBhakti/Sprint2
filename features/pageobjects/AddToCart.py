import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from Utilities.configreader import ConfigReader
from features.pageobjects.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Addtocart(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def OpenPage(self, url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)

    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("close_XPATH")

    def Click_loginhomepage(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_XPATH")

    def Enter_Username(self, username1):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH", username1)

    def Enter_password(self, password1):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("PASSWORD_XPATH", password1)

    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("loginbutton1_XPATH")

    def text_Searchbar(self, search1):
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")))
        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH", search1)

    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_XPATH")

    def Click_PRODUCT(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("PRODUCT_XPATH")
        time.sleep(5)

    def Click_ADDTOCART(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("ADDTOCART_XPATH")
        time.sleep(5)

    def Click_PLUSBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("PLUSBUTTON_XPATH")
        time.sleep(5)

    def Click_MINUSBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("MINUSBUTTON_XPATH")
        time.sleep(5)

    def Click_SAVEFORLATER(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SAVEFORLATER_XPATH")
        time.sleep(5)

    def Click_REMOVE(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("REMOVE_XPATH")
        time.sleep(5)





