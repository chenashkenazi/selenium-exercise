from WebDriver import WebDriver
from MongoDB import MongoDB
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time, requests


class BBCCrawler(WebDriver, MongoDB):

    def __init__(self, name, url, driver_location, binary_location):
        WebDriver.__init__(self, driver_location, binary_location, url)
        MongoDB.__init__(self, "mongodb://localhost:27017/")
        self.name = name

    def check_db_and_save(self, list_of_news):
        for new in list_of_news:
            if not self.check_existence("bbc", "title", new["title"]):
                self.insert("bbc", new)

    def get_new_details(self, new):
        title = new.text
        link = new.get_attribute('href')

        article = requests.get(link)
        soup = bs(article.content, 'html.parser')
        body = soup.find('article')
        if body:
            text = [p.text for p in body.find_all('p')]
            content = ' '.join(text)
            return title, link, content
        else:
            return None, None, None

    def parse_news(self, new):
        title, link, content = self.get_new_details(new)
        if title and link and content:
            record = {
                "title": title,
                "link": link,
                "content": content
            }
            return record

    def get_news_list(self):
        list_of_news = []
        self.webdriver()
        content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
        news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")
        for i in range(0, len(news)):
            new_record = self.parse_news(news[i])
            if new_record:
                list_of_news.append(new_record)
            content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
            news = content.find_elements(By.CLASS_NAME, "block-link__overlay-link")

        time.sleep(3)
        self.driver.quit()
        return list_of_news

    def download_content_and_save(self) -> object:
        list_of_news = self.get_news_list()
        print(list_of_news)
        self.check_db_and_save(list_of_news)

    def search_by_text(self, text):
        by_title = self.search("bbc", text, "title")
        by_content = self.search("bbc", text, "content")
        combined = by_title + by_content
        return [com['link'] for com in combined] if combined else None

