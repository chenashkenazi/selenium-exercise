from System import System

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

bbc_url = "https://www.bbc.com/"
#departures_flights_url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
#arrivals_flights_url = "https://www.iaa.gov.il/airports/ben-gurion/flight-board/?flightType=departures#tab-arrivel_flights1"

departures_flights_url = "https://www.iaa.gov.il/airports/ben-gurion/flight-board/"
arrivals_flights_url = None

remote_url_chrome = "http://172.25.0.2:4445/wd/hub"

if __name__ == "__main__":
    print("System is starting")
    system = System(bbc_url, remote_url_chrome, binary_location, departures_flights_url, arrivals_flights_url)
    system.consume()

