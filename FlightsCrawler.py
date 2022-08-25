from MongoDB import MongoDB
from WebDriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, requests
from bs4 import BeautifulSoup as bs


class FlightsCrawler(WebDriver, MongoDB):

    def __init__(self, name, url, driver_location, binary_location):
        WebDriver.__init__(self, driver_location, binary_location)
        MongoDB.__init__(self, "mongodb://localhost:27017/")
        self.name = name
        self.url = url

    def get_flights_list(self):
        self.webdriver()
        flights_website = requests.get(self.url)
        soup = bs(flights_website.content, 'html.parser')
        table = soup.find(id='flight_board-arrivel_table')

        headers = []
        for i in table.find_all("th"):
            title = i.text
            headers.append(title)



        time.sleep(3)
        self.driver.quit()

