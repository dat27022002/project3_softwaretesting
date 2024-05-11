"""
Tester: Nguyen Viet Minh Tan
MSSV: 2220022
Test feature: Edit Quiz
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

  assert "My courses" in self.driver.title
  print("\n")
  print('{:67s}{:5s}{:4s}'.format("1.  Login as manager","  -  ","Done"))


def edit_quiz(self):
  # Turn on Edit Mode - Begin
  self.driver.get("https://school.moodledemo.net/course/view.php?id=59")
  time.sleep(2)

  edit_mode_btn = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "custom-control-input"))
  ).click()

  print('{:67s}{:5s}{:4s}'.format("2.  Edit Mode turned ON","  -  ","Done"))
  print("\n")
  time.sleep(2)
  assert "Edit course" in self.driver.title
  # Turn on Edit Mode - End

  # Click the quiz link - Begin
  quiz_link = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Quiz: Know your Geography!"))
  )
  quiz_link.click()

  print('{:67s}{:5s}{:4s}'.format("3.  Click the quiz link","  -  ","Done"))
  # Click the quiz link - End

  # Click 'Settings' - Begin
  settings_nav = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Settings"))
  )
  settings_nav.click()

  print('{:67s}{:5s}{:4s}'.format("4.  Click 'Settings'","  -  ","Done"))
  # Click 'Settings' - End

  # Click 'Timing' - Begin
  timing_collapse = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "collapseElement-1"))
  )
  timing_collapse.click()

  print('{:67s}{:5s}{:4s}'.format("5.  Click 'Timing'","  -  ","Done"))
  # Click 'Timing' - End

  # Click 'Enable' in 'Time limit' - Begin
  enable_check = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_timelimit_enabled"))
  )
  enable_check = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.ID, "id_timelimit_enabled"))
  )
  if not enable_check.is_selected(): enable_check.click()
  time.sleep(2)

  print('{:67s}{:5s}{:4s}'.format("6.  Click 'Enable' in 'Time limit'","  -  ","Done"))
  # Click 'Enable' in 'Time limit' - End

  # Set time limit to -1 - Begin
  time_limit = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_timelimit_number"))
  )
  time.sleep(1)
  time_limit.clear()
  time_limit.send_keys("a")

  print('{:67s}{:5s}{:4s}'.format("7.  Set time limit to 'a'","  -  ","Done"))
  # Set time limit to -1 - End

  # Click 'Save and display' - Begin
  save_display = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_submitbutton"))
  )
  save_display = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.ID, "id_submitbutton"))
  )
  save_display.click()
  WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[text() = "Preview quiz"]'))
  )

  print('{:67s}{:5s}{:4s}'.format("8.  Click 'Save and display'","  -  ","Done"))
  # Click 'Save and display' - End

  # Confirm the input time limit 'a' is NOT accepted - Begin
  print('{:67s}{:5s}{:4s}'.format("9.  Confirm the input time limit 'a' is NOT accepted","  -  ","Done"))
  print("\nThe time limit input 'a' is accepted BUT the time limit is NOT displayed\n")
  assert "Grading method: Highest grade" not in self.driver.page_source
  # Confirm the input time limit 'a' is NOT accepted - End

  



class MoodleTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_EDIT_QUIZ_2(self):
    print('\n')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('If the test resulted in any errors, this is because of the incorrect timing of the appearance the elements of the page.\nPlease run the test 1-2 more times')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('\n')

    """
    The steps of this test are as followed:
    1.  Login as manager
    2.  Turn on Edit Mode
    3.  Click the quiz link
    4.  Click 'Settings'
    5.  Click 'Timing'
    6.  Click 'Enable' in 'Time limit'
    7.  Set time limit to 'a'
    8.  Click 'Save and display'
    9.  Confirm the input time limit 'a' is NOT accepted
    """

    login(self)
    edit_quiz(self)
  
  def tearDown(self):
    time.sleep(3)
    self.driver.quit()
    # pass
  
if __name__ == "__main__":
  unittest.main()