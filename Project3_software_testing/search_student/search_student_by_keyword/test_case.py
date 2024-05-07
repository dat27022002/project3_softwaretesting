import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

value1="ma"
value2="Mark Ellis"
value3="abc"

class Test_search_student(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://moodle.org/demo")
        self.login()
        driver=self.driver
        driver.implicitly_wait(10)
        
        course=driver.find_element(By.LINK_TEXT, "Moodle and Mountaineering")
        time.sleep(2)
        course.click()
        
        self.assertTrue("This course will introduce you to the basics of Alpine Mountaineering, while at the same time highlighting some of the great features of Moodle." in self.driver.page_source) 
        navigation=driver.find_element(By.CLASS_NAME, "secondary-navigation")
        button_setting=navigation.find_element(By.LINK_TEXT, "Participants")
        button_setting.click()
        
        self.assertTrue("With selected users..." in self.driver.page_source)
         

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
          
         
    "Searching for keywords to get results gets a lot of students"
    def test_to_get_lots_of_students(self): 
        driver=self.driver
        
        select = Select(driver.find_element(By.CSS_SELECTOR, '.custom-select.my-1.mb-md-0.mr-md-2'))
        select.select_by_value("keywords")
        container_input_keyword=driver.find_element(By.CSS_SELECTOR, ".form-autocomplete-input.d-md-inline-block.mr-md-2")
        
        input_keyword=container_input_keyword.find_element(By.TAG_NAME,'input')
        input_keyword.clear()
        input_keyword.send_keys(value1)
        input_keyword.send_keys(Keys.RETURN)
        
        
        button_apply=driver.find_element(By.XPATH,"//*[text()='Apply filters']")
        button_apply.click()
        
        time.sleep(2)
        
        table=driver.find_element(By.ID,"participants")
        body_table=table.find_element(By.TAG_NAME,'tbody')
        items=body_table.find_elements(By.TAG_NAME,"tr")
            
        items = [item for item in items if item.get_attribute('class') == '']
        
        self.assertTrue(len(items)>1)
        
        for item in items:
            name=item.find_element(By.CLASS_NAME,"c1")
            self.assertTrue(value1.lower() in name.get_attribute('textContent').lower())
       
    "Search keywords to get results of 1 student"
    def test_to_get_a_student(self): 
        driver=self.driver
        
        select = Select(driver.find_element(By.CSS_SELECTOR, '.custom-select.my-1.mb-md-0.mr-md-2'))
        select.select_by_value("keywords")
        container_input_keyword=driver.find_element(By.CSS_SELECTOR, ".form-autocomplete-input.d-md-inline-block.mr-md-2")
        
        input_keyword=container_input_keyword.find_element(By.TAG_NAME,'input')
        input_keyword.clear()
        input_keyword.send_keys(value2)
        input_keyword.send_keys(Keys.RETURN)
        
        
        button_apply=driver.find_element(By.XPATH,"//*[text()='Apply filters']")
        button_apply.click()
        
        time.sleep(2)
        
        table=driver.find_element(By.ID,"participants")
        body_table=table.find_element(By.TAG_NAME,'tbody')
        items=body_table.find_elements(By.TAG_NAME,"tr")
            
        items = [item for item in items if item.get_attribute('class') == '']
        
        self.assertTrue(len(items)==1)
        
        for item in items:
            name=item.find_element(By.CLASS_NAME,"c1")
            self.assertTrue(value1.lower() in name.get_attribute('textContent').lower())
    
    "Keyword search results in no students"
    def test_to_get_no_student(self): 
        driver=self.driver
        
        select = Select(driver.find_element(By.CSS_SELECTOR, '.custom-select.my-1.mb-md-0.mr-md-2'))
        select.select_by_value("keywords")
        container_input_keyword=driver.find_element(By.CSS_SELECTOR, ".form-autocomplete-input.d-md-inline-block.mr-md-2")
        
        input_keyword=container_input_keyword.find_element(By.TAG_NAME,'input')
        input_keyword.clear()
        input_keyword.send_keys(value3)
        input_keyword.send_keys(Keys.RETURN)
        
        
        button_apply=driver.find_element(By.XPATH,"//*[text()='Apply filters']")
        button_apply.click()
        
        time.sleep(2)
        
        self.assertTrue("Nothing to display" in driver.page_source)
        
      
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)