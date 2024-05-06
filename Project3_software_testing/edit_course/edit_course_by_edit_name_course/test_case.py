import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_edit_course(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://moodle.org/demo")
        self.login()

    def login(self):
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
        time.sleep(1)
        input_password=driver.find_element(By.NAME, "password")
        input_password.clear()
        input_password.send_keys("moodle")
        button_handle_login=driver.find_element(By.ID, "loginbtn")
        button_handle_login.click()
        
        self.assertTrue("Course overview" in self.driver.page_source)
        
    "Testcase with valid name course"
    def test_edit_course_success(self): 
        driver=self.driver
        driver.implicitly_wait(10)
        
        course=driver.find_element(By.LINK_TEXT, "Moodle and Mountaineering")
        time.sleep(2)
        course.click()
        
        self.assertTrue("This course will introduce you to the basics of Alpine Mountaineering, while at the same time highlighting some of the great features of Moodle." in self.driver.page_source)  
        navigation=driver.find_element(By.CLASS_NAME, "secondary-navigation")
        button_setting=navigation.find_element(By.LINK_TEXT, "Settings")
        button_setting.click()
        
        self.assertTrue("Edit course settings" in self.driver.page_source)
        input_fullname=driver.find_element(By.NAME, "fullname")
        input_fullname.clear()
        input_fullname.send_keys("Moodle and Mountaineering 2.0")
        button_save=driver.find_element(By.NAME, "saveanddisplay")
        button_save.click()
        
        self.assertTrue("This course will introduce you to the basics of Alpine Mountaineering, while at the same time highlighting some of the great features of Moodle." in self.driver.page_source)  
        navigation=driver.find_element(By.CLASS_NAME, "secondary-navigation")
        button_setting=navigation.find_element(By.LINK_TEXT, "Settings")
        button_setting.click()
        
        self.assertTrue("Edit course settings" in self.driver.page_source)
        input_fullname=driver.find_element(By.NAME, "fullname")
        input_fullname.clear()
        input_fullname.send_keys("Moodle and Mountaineering")
        button_save=driver.find_element(By.NAME, "saveanddisplay")
        button_save.click()
        
         
    "Testcase with emtpy name course"
    def test_edit_course_fail(self): 
        driver=self.driver
        driver.implicitly_wait(10)
        
        course=driver.find_element(By.LINK_TEXT, "Moodle and Mountaineering")
        time.sleep(2)
        course.click()
        
        self.assertTrue("This course will introduce you to the basics of Alpine Mountaineering, while at the same time highlighting some of the great features of Moodle." in self.driver.page_source)  
        navigation=driver.find_element(By.CLASS_NAME, "secondary-navigation")
        button_setting=navigation.find_element(By.LINK_TEXT, "Settings")
        button_setting.click()
        
        self.assertTrue("Edit course settings" in self.driver.page_source)
        input_fullname=driver.find_element(By.NAME, "fullname")
        input_fullname.clear()
        button_save=driver.find_element(By.NAME, "saveanddisplay")
        button_save.click()
        
        self.assertTrue("Missing full name" in self.driver.page_source)  
          
      
          
   
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)