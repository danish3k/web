import selenium
from selenium import webdriver
#from Web_Test import yamlparser

class web_test():
    driver = webdriver.Chrome()
    def __init__(self):
        pass

    def launch(self):
        self.driver.maximize_window()
        self.driver.get(url='https://google.com')
    def close(self):
        self.driver.close()

#web_test().launch()
#web_test().close()