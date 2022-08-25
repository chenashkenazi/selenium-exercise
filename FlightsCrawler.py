from MongoDB import MongoDB
from WebDriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class FlightsCrawler(WebDriver, MongoDB):

    def __init__(self, name, url, driver_location, binary_location):
        WebDriver.__init__(self, driver_location, binary_location)
        MongoDB.__init__(self, "mongodb://localhost:27017/")
        self.name = name
        self.url = url

    def get_flights_list(self):
        self.webdriver()
        flights = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "flight_board - arrivel_table")))
        # news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")
        # for i in range(0, len(news)):
        #     self.parse_news(news[i])
        #     content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
        #     news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")
        print(flights)
        time.sleep(3)
        self.driver.quit()

