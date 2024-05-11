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

  # Dublicate the current window in a new tab & switch focus - Begin
  original_window = self.driver.current_window_handle
  login_url = self.driver.current_url

  self.driver.switch_to.new_window('tab')
  wait.until(EC.number_of_windows_to_be(2))

  for window_handle in self.driver.window_handles:
        if window_handle != original_window:
            self.driver.switch_to.window(window_handle)
            break
        
  self.driver.get(login_url)
  wait.until(EC.title_is('My courses | Mount Orange School'))

  print('{:67s}{:5s}{:4s}'.format("2.  Dublicate the current window in a new tab","  -  ","Done"))
  # Dublicate the current window in a new tab & switch focus - End
  
  # Log out - Begin
  #Click the profile image
  wait.until(EC.element_to_be_clickable((By.ID, 'user-menu-toggle'))).click()

  #Click Log out
  wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log out'))).click()

  #Wait for the log out page to completely load
  wait.until(EC.title_contains('Home | Mount Orange School'))

  print('{:67s}{:5s}{:4s}'.format("3.  Log out","  -  ","Done"))
  # Log out - End

  # Access profile information in first tab - Begin
  self.driver.switch_to.window(original_window)
  #Click the profile image
  wait.until(EC.element_to_be_clickable((By.ID, 'user-menu-toggle'))).click()

  #Click Profile
  wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Profile'))).click()

  print('{:67s}{:5s}{:4s}'.format("4.  Click Profile","  -  ","Done"))
  # Access profile information in first tab - End

  # Confirm access denied - Begin
  assert 'Guests cannot access user profiles' in self.driver.page_source

  print('{:67s}{:5s}{:4s}'.format("5.  Confirm access denied","  -  ","Done"))
  # Confirm access denied - End
  



class MoodleTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    pass

  def test_ACCESS_SECURITY_2(self):
    print('\n')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('If the test resulted in any errors, this is because of the incorrect timing of the appearance the elements of the page.\nPlease run the test 1-2 more times')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('\n')

    """
    The steps of this test are as followed:
    1.  Login as manager
    2.  Dublicate the current window in a new tab & switch focus
    3.  Log out
    4.  Click Profile
    5.  Confirm access denied
    """

    login(self)
    access_security(self)
  
  def tearDown(self):
    time.sleep(3)
    self.driver.quit()
    # pass
  
if __name__ == "__main__":
  unittest.main()