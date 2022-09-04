import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WebDriver:

    def __init__(self, driver_location, binary_location, url):
        self.driver_location = driver_location
        self.binary_location = binary_location
        self.url = url
        self.driver = None

    def webdriver(self):
        attemps = 0
        while attemps < 10:
            try:
                print("Creating webdriver in 5 seconds")
                time.sleep(5)

                print("Remote")
                driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',
                                          desired_capabilities=DesiredCapabilities.CHROME)
                print("get url")
                driver.get(self.url)

                self.driver = driver
                break
            except Exception as ex:
                print(ex)
                print("Failed. try again!")
                attemps += 1



