import selenium
from selenium import webdriver
from Web_Test import yamlparser

class web_test():
    driver = webdriver.Chrome()
    val = yamlparser.read_yaml()
    def __init__(self):
        pass

    def launch(self):
        website = self.val.read_yaml_all()

        self.driver.maximize_window()
        self.driver.get(url=website['url'])
        company_name = self.driver.find_element_by_xpath(website['company']).text
        return company_name
    def close(self):
        self.driver.close()

#A = web_test().launch()
#print(A)
#web_test().close()