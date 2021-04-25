from selenium import webdriver


class WebDrivers:
    def __init__(self, web):
        self.driver = web
        if web == "SM":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

        elif web == "fire":
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()

        elif web == "edge":
            self.driver = webdriver.Edge()
        else:
            print(f"{web} Not Found!!")

    def run_page(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
