from selenium import webdriver
from BBCCrawler import BBCCrawler
from FlightsCrawler import FlightsCrawler

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

bbc_url = "https://www.bbc.com/"
departures_flights_url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
arrivals_flights_url = "https://www.iaa.gov.il/airports/ben-gurion/flight-board/?flightType=departures#tab-arrivel_flights1"

if __name__ == "__main__":
    bbc_crl = BBCCrawler("bbc", bbc_url, driver_location, binary_location)
    departures_flights_crl = FlightsCrawler("flights", departures_flights_url, driver_location, binary_location)
    arrivals_flights_crl = FlightsCrawler("flights", arrivals_flights_url, driver_location, binary_location)

    bbc_crl.get_news_list()
    # departures_flights_crl.get_flights_list()
    # arrivals_flights_crl.get_flights_list()

