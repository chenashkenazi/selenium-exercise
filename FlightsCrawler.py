from MongoDB import MongoDB
from WebDriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FlightsCrawler(WebDriver, MongoDB):

    def __init__(self, name, url, driver_location, binary_location):
        WebDriver.__init__(self, driver_location, binary_location, url)
        MongoDB.__init__(self, "mongodb://localhost:27017/")
        self.name = name

    def check_db_and_save(self, list_of_flights):
        for flight in list_of_flights:
            if not self.check_existence("flights", "flight", flight["flight"]):
                self.insert("flights", flight)

    def get_flights_list(self):
        self.webdriver()
        if "arrivel" in self.driver.current_url:
            tbody_num = 1
        else:
            tbody_num = 0

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flight_row")))
            table = self.driver.find_element(By.CLASS_NAME, "tabs-content")
            tbody2 = table.find_elements(By.TAG_NAME, "tbody")
            self.driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})

            table_rows = tbody2[tbody_num].find_elements(By.CLASS_NAME, "flight_row")

            list_of_flights = []
            for row in table_rows:
                dict_of_row = {}
                airline = row.find_element(By.CLASS_NAME, "td-airline")
                airline_text = airline.get_attribute("innerHTML")
                dict_of_row['airline'] = airline_text

                flight = row.find_element(By.CLASS_NAME, "td-flight")
                flight_text = flight.get_attribute("innerHTML")
                dict_of_row['flight'] = flight_text

                city = row.find_element(By.CLASS_NAME, "td-city")
                city_text = city.get_attribute("innerHTML")
                dict_of_row['city'] = city_text

                terminal = row.find_element(By.CLASS_NAME, "td-terminal")
                terminal_text = terminal.get_attribute("innerHTML")
                dict_of_row['terminal'] = terminal_text

                scheduled_time = row.find_element(By.CLASS_NAME, "td-scheduledTime")
                scheduled_time_date = scheduled_time.find_element(By.TAG_NAME, "strong").get_attribute("innerHTML")
                scheduled_time_time = scheduled_time.find_element(By.TAG_NAME, "div").get_attribute("innerHTML")
                scheduled_time_text = f"{scheduled_time_date} {scheduled_time_time}"
                dict_of_row['scheduled_time'] = scheduled_time_text

                updated_time = row.find_element(By.CLASS_NAME, "td-updatedTime")
                updated_time_text = updated_time.find_element(By.TAG_NAME, "time").get_attribute("innerHTML")
                dict_of_row['updated_time'] = updated_time_text

                status = row.find_element(By.CLASS_NAME, "row-status")
                status_text = status.find_element(By.TAG_NAME, "div").get_attribute("innerHTML")
                dict_of_row['status'] = status_text

                list_of_flights.append(dict_of_row)

            print(list_of_flights)
            return list_of_flights

        except:
            self.get_flights_list()

    def download_content_and_save(self):
        flights_list = self.get_flights_list()
        self.check_db_and_save(flights_list)





