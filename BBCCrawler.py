from WebDriver import WebDriver
from MongoDB import MongoDB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time, requests


class BBCCrawler(WebDriver, MongoDB):

    def __init__(self, name, url, driver_location, binary_location):
        WebDriver.__init__(self, driver_location, binary_location)
        MongoDB.__init__(self, "mongodb://localhost:27017/")
        self.name = name
        self.url = url

    def get_new_details(self, new):
        title = new.text
        link = new.get_attribute('href')

        article = requests.get(link)
        soup = bs(article.content, 'html.parser')
        body = soup.find('article')
        text = [p.text for p in body.find_all('p')]
        content = ' '.join(text)
        print(content)

        return title, link, content

    def parse_news(self, new):
        title, link, content = self.get_new_details(new)
        record = {
            "title": title,
            "link": link,
            "content": content
        }
        print(record)
        # save(record)
        # self.insert("bbc", record)

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




