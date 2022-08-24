from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class Crawler:

    def __init__(self, name, url, driver_location, binary_location):
        self.name = name
        self.url = url
        self.driver_location = driver_location
        self.binary_location = binary_location
        self.driver = None

    def webdriver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.binary_location

        driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=options)
        driver.get(self.url)

        self.driver = driver

    def parse_bbc(self, new):
        title = new.text
        link = new.get_attribute('href')
        full_new = new.click()
        try:
            # full_new = WebDriverWait(new, 10)
            # print(new.page_source.encode("utf-8"))
            main = full_new.find_elements(By.CLASS_NAME, "edr_survey")
            print(f"full new: {main}")
        except:
            print("didnt find")
            self.driver.execute_script("window.history.go(-1)")
            return


    def get_list(self):
        self.webdriver()
        print(self.driver.page_source.encode("utf-8"))
        content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
        news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")
        for i in range(0, len(news)):
            self.parse_bbc(news[i])
            content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
            news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")
        # self.parse_bbc(news)
        # print(new.text)
        # print(new.get_attribute('href'))

        time.sleep(3)
        self.driver.quit()



