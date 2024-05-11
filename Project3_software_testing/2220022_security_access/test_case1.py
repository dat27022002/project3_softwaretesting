"""
Tester: Nguyen Viet Minh Tan
MSSV: 2220022
Test feature: Access Security
"""

import unittest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller, Key
import time

def login(self):
  self.driver.get("https://school.moodledemo.net/login/index.php")

  username = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
  )
  username.clear()
  username.send_keys("manager")

  password = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
  )
  password.clear()
  password.send_keys("moodle")

  login_btn = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "loginbtn"))
  )
  login_btn.click()

  wait = WebDriverWait(self.driver, 10)
  wait.until(EC.title_is('My courses | Mount Orange School'))

  assert "My courses" in self.driver.title
  print("\n")
  print('{:67s}{:5s}{:4s}'.format("1.  Login as manager","  -  ","Done"))


def access_security(self):
  wait = WebDriverWait(self.driver, 10)

  # Access profile information
  wait.until(EC.element_to_be_clickable((By.ID, 'user-menu-toggle'))).click()
  print('{:67s}{:5s}{:4s}'.format("2.  Access profile information","  -  ","Done"))

  # Click 'Profile'
  wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Profile'))).click()
  print('{:67s}{:5s}{:4s}'.format("3.  'Click Profile'","  -  ","Done"))

  # Click 'Edit profile'
  wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Edit profile'))).click()
  print('{:67s}{:5s}{:4s}'.format("4.  Click 'Edit profile'","  -  ","Done"))

  # Change email
  email = wait.until(EC.presence_of_element_located((By.ID, 'id_email')))
  email.clear()
  email.send_keys('annaalexand246@example.com')
  print('{:67s}{:5s}{:4s}'.format("5.  Change email","  -  ","Done"))

  # Click 'Update profile'
  self.driver.find_element(By.ID, 'id_submitbutton').click()
  print('{:67s}{:5s}{:4s}'.format("6.  Click 'Update profile'","  -  ","Done"))

  # Confirm changes made
  assert 'Changes saved' in self.driver.page_source
  print('{:67s}{:5s}{:4s}'.format("7.  Confirm changes made","  -  ","Done"))
  



class MoodleTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    pass

  def test_ACCESS_SECURITY_1(self):
    print('\n')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('If the test resulted in any errors, this is because of the incorrect timing of the appearance the elements of the page.\nPlease run the test 1-2 more times')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('\n')

    """
    The steps of this test are as followed:
    1.  Login as manager
    2.  Access profile information
    3.  Click 'Profile'
    4.  Click 'Edit profile'
    5.  Change email
    6.  Click 'Update profile'
    7.  Confirm changes made
    """

    login(self)
    access_security(self)
  
  def tearDown(self):
    time.sleep(3)
    self.driver.quit()
    # pass
  
if __name__ == "__main__":
  unittest.main()