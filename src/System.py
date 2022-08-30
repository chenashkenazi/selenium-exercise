from kafka import KafkaConsumer
import json
from BBCCrawler import BBCCrawler
from FlightsCrawler import FlightsCrawler


class System:
    def __init__(self, bbc_url, driver_location, binary_location, departures_flights_url, arrivals_flights_url):
        self.consumer = KafkaConsumer('exercise', bootstrap_servers='127.0.0.1:29092', api_version=(0,10))
        self.bbc_crl = BBCCrawler("bbc", bbc_url, driver_location, binary_location)
        self.departures_flights_crl = FlightsCrawler("flights", departures_flights_url, driver_location, binary_location)
        self.arrivals_flights_crl = FlightsCrawler("flights", arrivals_flights_url, driver_location, binary_location)

    def parse_command(self, command):
        result = None
        if command["crl"] == "bbc":
            if command["action"] == "download_save":
                self.bbc_crl.download_content_and_save()
            elif command["action"] == "search":
                text = command["search"]["text"]
                result = self.bbc_crl.search_by_text(text)
        elif command["crl"] == "flights":
            if command["action"] == "download_save":
                self.departures_flights_crl.download_content_and_save()
                self.arrivals_flights_crl.download_content_and_save()
            elif command["action"] == "search":
                text = command["search"]["text"]
                field = command["search"]["field"]
                result = self.departures_flights_crl.search_by_text(text, field)
        print(result)

    def consume(self):
        print("I am consuming")
        for event in self.consumer:
            message = json.loads(event.value.decode("ascii"))
            self.parse_command(message)
        print("I am done")



