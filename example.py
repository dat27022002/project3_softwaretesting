from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert

PATH = "C:\Program Files (x86)\chromedriver.exe"
service = webdriver.ChromeService(executable_path = PATH)
driver = webdriver.Chrome()

driver.get("http://www.python.org")


time.sleep(5)
driver.close()
