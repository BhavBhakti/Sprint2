import time
from features.pageobjects.Base import BaseSettingsPage
from selenium.webdriver.common.by import By
import random


class Product(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

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
        self.driver.execute_script("window.scrollBy(0,350)")
        #self.driver.find_element(By.CLASS_NAME,"_2jufoV").click()
        self.ClickButton("productplus_CLASS")
        time.sleep(5)
        self.ClickButton("productplus_CLASS")
        time.sleep(5)

    def addtocart(self):
        self.ClickButton("addtocartbutton_XPATH")
        time.sleep(5)

    def placeorder(self, expectedTextVal):
        self.AssertText("placeorderbutton_XPATH", expectedTextVal)
        time.sleep(5)
