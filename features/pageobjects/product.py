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


class Product(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def searchbox(self, search):
        # self.TypeEditBox("searchbox_NAME",search)
        self.DynamicImplicitWait(40)
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")))
        self.DynamicImplicitWait(40)
        self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(search)

    def clicksearch(self):
        # self.ClickButton("searchbutton_XPATH")
        self.DynamicImplicitWait(40)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
        time.sleep(10)

    def clickTop(self):
        top = self.driver.find_elements(By.CLASS_NAME, "_2r_T1I")
        c = random.choice(top)
        c.click()
        time.sleep(5)

    def winswitch(self):
        w2 = self.driver.window_handles[1]
        self.driver.switch_to.window(w2)
        time.sleep(5)

    def switchimages(self):
        img = self.driver.find_elements(By.CLASS_NAME, "_1AuMiq")
        for i in img:
            i.click()
            time.sleep(5)

    def enterpin(self, pincode):
        self.TypeEditBox("enterpin_CLASS", pincode)
        time.sleep(3)

    def clickcheck(self):
        self.ClickLinks("check_CLASS")
        time.sleep(5)

    def colour(self):
        try:
            cl = self.driver.find_elements(By.CLASS_NAME, "_2C41yO")
            c = random.choice(cl)
            c.click()
        except:
            pass
        time.sleep(5)

    def size(self):
        s = self.driver.find_elements(By.CLASS_NAME, "_1fGeJ5")
        c = random.choice(s)
        c.click()
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(5)

    def productplus(self):
        p = self.driver.find_element(By.CLASS_NAME,"_2jufoV").click()
        self.driver.execute_script("window.scrollBy(0,600)")
        time.sleep(5)

    def addtocart(self):
        self.ClickButton("addtocartbutton_XPATH")
        time.sleep(5)

    def placeorder(self, expectedTextVal):
        self.AssertText("placeorderbutton_XPATH", expectedTextVal)
        time.sleep(5)
