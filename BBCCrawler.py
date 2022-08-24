from WebDriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class BBCCrawler(WebDriver):

    def __init__(self, name, url, driver_location, binary_location):
        WebDriver.__init__(self, driver_location, binary_location)
        self.name = name
        self.url = url


    def get_new_details(self, new):
        title = new.text
        link = new.get_attribute('href')
        new.click()
        try:
            # full_new = WebDriverWait(new, 10)
            # print(new.page_source.encode("utf-8"))
            full_new = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "root")))
            main = full_new.find_element(By.ID, "main-content")
            span = main.find_element(By.XPATH, '//*[@id="main-content"]/div[5]/div/div[1]/article/header/p')
            print(f"full new: {span.text}")
            self.driver.execute_script("window.history.go(-1)")
        except:
            print("didnt find")
            self.driver.execute_script("window.history.go(-1)")
            return

    def get_news_list(self):
        self.webdriver()
        content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
        news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")
        for i in range(0, len(news)):
            self.parse_news(news[i])
            content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
            news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")

        time.sleep(3)
        self.driver.quit()



