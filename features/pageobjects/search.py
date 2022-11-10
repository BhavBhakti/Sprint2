import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from features.pageobjects.Base import BaseSettingsPage
from Utilities.configreader import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random


class Search(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def searchbox(self, search):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("searchbox_NAME",search)
        # WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")))
        # self.DynamicImplicitWait(40)
        #self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(search)

    def clicksearch(self):
        self.DynamicImplicitWait(40)
        #self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
        self.ClickButton("searchbutton_XPATH")
        time.sleep(10)