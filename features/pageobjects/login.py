import time

from selenium import webdriver
from features.pageobjects.Base import BaseSettingsPage
from Utilities.configreader import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class login(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)

    def fliphome(self):
        self.driver.get(ConfigReader("base info","URL"))

    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("closeloginwindow_XPATH")
        time.sleep(1)

    def clickloginLink(self):
        self.ClickLinks("loginLink_XPATH")

    def logmobno(self,numberr):
        self.TypeEditBox("loginMobileNo_XPATH",numberr)

    def logpassword(self,passwordd):
        self.TypeEditBox("loginpassword_XPATH",passwordd)

    def signinbutton(self):
        self.ClickButton("SignInButton_XPATH")
        time.sleep(10)