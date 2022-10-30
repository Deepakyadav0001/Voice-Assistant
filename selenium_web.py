from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class wiki():
    def __int__(self):
        serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
    def search(self,query):
        serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.wikipedia.org/")
        self.driver.maximize_window()
        search=self.driver.find_element(By.XPATH,"//*[@id='searchInput']")
        search.click()
        search.send_keys(query)
        self.driver.find_element(By.XPATH,"//*[@id='search-form']/fieldset/button").click()

