from selenium import webdriver
from BBCCrawler import BBCCrawler
from FlightsCrawler import FlightsCrawler

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

bbc_url = "https://www.bbc.com/"
flights_url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"

if __name__ == "__main__":
    bbc_crl = BBCCrawler("bbc", bbc_url, driver_location, binary_location)
    flights_crl = FlightsCrawler("flights", flights_url, driver_location, binary_location)

    # bbc_crl.get_news_list()
    flights_crl.get_flights_list()

