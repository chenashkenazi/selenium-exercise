from selenium import webdriver
from BBCCrawler import BBCCrawler

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

if __name__ == "__main__":
    bbc_crl = BBCCrawler("bbc", "https://www.bbc.com/", driver_location, binary_location)

    bbc_crl.get_news_list()

