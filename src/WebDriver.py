from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"


class WebDriver:

    def __init__(self, driver_location, binary_location, url):
        self.driver_location = driver_location
        self.binary_location = binary_location
        self.url = url
        self.driver = None

    def webdriver(self):
        # captcha
        # options = Options()
        # ua = UserAgent()
        # userAgent = ua.random
        # print(userAgent)
        # options.add_argument(f'user-agent={userAgent}')
        # driver = webdriver.Chrome(chrome_options=options,
        #                           executable_path=PATH)
        # driver.get(self.url)
        # self.driver = driver

        options = webdriver.ChromeOptions()
        options.binary_location = self.binary_location

        driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=options)
        driver.get(self.url)

        self.driver = driver
