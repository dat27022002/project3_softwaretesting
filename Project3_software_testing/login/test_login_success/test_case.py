import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://moodle.org/demo")

    def test_login_success(self):
        driver=self.driver
        button_mount_orange_school=driver.find_element(By.LINK_TEXT, "Mount Orange School")
        button_mount_orange_school.click()
        
        self.assertTrue("Try Moodle in a real-school environment with ready-made accounts" in self.driver.page_source)
        button_login=driver.find_element(By.LINK_TEXT, "Log in")
        button_login.click()
        
        self.assertTrue("Lost password?" in self.driver.page_source)
        input_username=driver.find_element(By.NAME, "username")
        input_username.clear()
        input_username.send_keys("teacher")
        input_password=driver.find_element(By.NAME, "password")
        input_password.clear()
        input_password.send_keys("moodle")
        button_handle_login=driver.find_element(By.ID, "loginbtn")
        button_handle_login.click()
        
        self.assertTrue("Course overview" in self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)