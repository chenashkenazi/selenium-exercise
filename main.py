from System import System

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

bbc_url = "https://www.bbc.com/"
departures_flights_url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
arrivals_flights_url = "https://www.iaa.gov.il/airports/ben-gurion/flight-board/?flightType=departures#tab-arrivel_flights1"

if __name__ == "__main__":
    system = System(bbc_url, driver_location, binary_location, departures_flights_url, arrivals_flights_url)
    system.consume()

