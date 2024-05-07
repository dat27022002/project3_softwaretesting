import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

username_correct="teacher"
password_correct="moodle"
username_wrong="teacher1"
password_wrong="moodle1"

class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://moodle.org/demo")
        driver=self.driver
        button_mount_orange_school=driver.find_element(By.LINK_TEXT, "Mount Orange School")
        button_mount_orange_school.click()
        
        self.assertTrue("Try Moodle in a real-school environment with ready-made accounts" in self.driver.page_source)
        button_login=driver.find_element(By.LINK_TEXT, "Log in")
        button_login.click()
        
        self.assertTrue("Lost password?" in self.driver.page_source)

    "Testcase with valid username and valid password."
    def test_login_success(self):
        driver=self.driver

        self.assertTrue("Lost password?" in self.driver.page_source)
        input_username=driver.find_element(By.NAME, "username")
        input_username.clear()
        input_username.send_keys(username_correct)
        time.sleep(1)
        input_password=driver.find_element(By.NAME, 'password')
        input_password.clear()
        input_password.send_keys(password_correct)
        button_handle_login=driver.find_element(By.ID, "loginbtn")
        button_handle_login.click()
        
        self.assertTrue("Course overview" in self.driver.page_source)


    "Testcase with valid username and wrong password."
    def test_login_fail_with_wrong_password(self):
        driver=self.driver
        input_username=driver.find_element(By.NAME, "username")
        input_username.clear()
        input_username.send_keys(username_correct)
        time.sleep(1)
        input_password=driver.find_element(By.NAME, "password")
        input_password.clear()
        input_password.send_keys(password_wrong)
        button_handle_login=driver.find_element(By.ID, "loginbtn")
        button_handle_login.click()
       
        self.assertTrue("Invalid login, please try again" in self.driver.page_source)
    
    "Testcase with invalid username and correct password."
    def test_login_fail_with_wrong_username(self):
        driver=self.driver
        input_username=driver.find_element(By.NAME, "username")
        input_username.clear()
        input_username.send_keys(username_wrong)
        time.sleep(1)
        input_password=driver.find_element(By.NAME, "password")
        input_password.clear()
        input_password.send_keys(password_correct)
        button_handle_login=driver.find_element(By.ID, "loginbtn")
        button_handle_login.click()
       
        self.assertTrue("Invalid login, please try again" in self.driver.page_source) 
        
    "Testcase with invalid username and wrong password."
    def test_login_fail_with_wrong_username_and_wrong_password(self):
        driver=self.driver
        input_username=driver.find_element(By.NAME, "username")
        input_username.clear()
        input_username.send_keys(username_wrong)
        time.sleep(1)
        input_password=driver.find_element(By.NAME, "password")
        input_password.clear()
        input_password.send_keys(password_wrong)
        button_handle_login=driver.find_element(By.ID, "loginbtn")
        button_handle_login.click()
       
        self.assertTrue("Invalid login, please try again" in self.driver.page_source)   
    
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)