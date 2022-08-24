from selenium import webdriver
from Crawler import Crawler

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

if __name__ == "__main__":
    bbc_crl = Crawler("bbc", "https://www.bbc.com/", driver_location, binary_location)
    flights_crl = Crawler("flights", "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx", driver_location, binary_location)

    bbc_crl.get_list()

