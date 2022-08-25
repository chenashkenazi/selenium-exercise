from WebDriver import WebDriver
from MongoDB import MongoDB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class BBCCrawler(WebDriver, MongoDB):

    def __init__(self, name, url, driver_location, binary_location):
        WebDriver.__init__(self, driver_location, binary_location)
        self.name = name
        self.url = url

    def get_new_content(self, new):
        content = ""
        print(new.parent.page_source)
        try:
            # text_blocks = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.TAG_NAME, "article"))
            text_blocks_div = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CLASS_NAME, "ssrcss-uf6wea-RichTextComponentWrapper ep2nwvo0"))
            text_blocks = text_blocks_div.find_elements(By.CLASS_NAME, "ssrcss-7uxr49-RichTextContainer e5tfeyi1")
            for block in text_blocks:
                content += block.find_element(By.CLASS_NAME, "ssrcss-1q0x1qg-Paragraph eq5iqo00").text
            return content
        except:
            print("didnt find")
            self.driver.execute_script("window.history.go(-1)")
            return content

    def get_new_details(self, new):
        title = new.text
        link = new.get_attribute('href')
        new.click()
        try:
            author = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, '//*[@id="main-content"]/div[5]/div/div[1]/article/header/p'))
            self.driver.execute_script("window.history.go(-1)")
            return title, link, author
        except:
            print("didnt find")
            return title, link, None

    def parse_news(self, new):
        title, link, author = self.get_new_details(new)
        content = self.get_new_content(new)
        record = {
            "title": title,
            "link": link,
            "author": author,
            "content": content
        }
        print(record)
        # save(record)
        self.insert("bbc", record)

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




