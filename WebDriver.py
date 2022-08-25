from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

class WebDriver:

    def __init__(self, driver_location, binary_location):
        self.driver_location = driver_location
        self.binary_location = binary_location
        self.driver = None

    def webdriver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.binary_location

        # driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=options)
        driver = webdriver.Chrome(PATH)
        driver.get(self.url)

        self.driver = driver
