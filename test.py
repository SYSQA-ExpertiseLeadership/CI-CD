from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time



class TestClass():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def WaitX(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        waituntil = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        return waituntil

    def go_to_clickcounter(self):
        clicker = '//*[@id="counter1"]/div[4]/div[1]/div[2]'
        self.driver.get('https://tallycounterstore.com/online-counter')
        self.WaitX(clicker)

    def click_on_counter(self):
        clicker = '//*[@id="counter1"]/div[4]/div[1]/div[2]'
        click_counter = '//*[@id="counter1"]/div[3]/div[2]'
        self.WaitX(clicker).click()
        text = self.WaitX(click_counter).text
        print(text)

    def repeat(self):
        while True:
            self.click_on_counter()


test = TestClass()
test.go_to_clickcounter()
test.click_on_counter()



