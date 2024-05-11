"""
Tester: Nguyen Viet Minh Tan
MSSV: 2220022
Test feature: View Quiz
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

  username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
  username.clear()
  username.send_keys("manager")

  password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
  password.clear()
  password.send_keys("moodle")

  login_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "loginbtn")))
  login_btn.click()

  assert "My courses" in self.driver.title
  print("\n")
  print('{:78s}{:5s}{:4s}'.format("1.  Login as manager","  -  ","Done"))


def view_quiz_result(self):
  # Go to a predetermined course - Begin
  self.driver.get("https://school.moodledemo.net/course/view.php?id=71")
  time.sleep(2)
  print('{:78s}{:5s}{:4s}'.format("2.  Go to a predetermined course","  -  ","Done"))
  # Go to a predetermined course - End

  # Turn on Edit Mode - Begin
  edit_mode_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "custom-control-input")))
  edit_mode_btn.click()

  print('{:78s}{:5s}{:4s}'.format("3.  Edit Mode turned ON","  -  ","Done"))
  print("\n")
  time.sleep(2)
  assert "Edit course" in self.driver.title
  # Turn on Edit Mode - End

  # Click 'Module 1 quick check' - Begin
  quiz_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Module 1 quick")))
  quiz_1.click()

  print('{:78s}{:5s}{:4s}'.format("4.  Click 'Module 1 quick check'","  -  ","Done"))
  # Click 'Module 1 quick check' - End

  # Click 'Results' - Begin
  results = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Results")))
  results.click()

  print('{:78s}{:5s}{:4s}'.format("5.  Click 'Results'","  -  ","Done"))
  # Click 'Results' - End

  # In 'Attemps that are: just leave 'Never Submitted', 'Finished' unchecked, the rest are checked - Begin
  attemps_id = ['id_stateinprogress', 'id_stateoverdue', 'id_statefinished', 'id_stateabandoned']
  for attemp in attemps_id:
    if attemp == 'id_stateabandoned' or attemp == 'id_statefinished':
      never_submitted = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, attemp)))
      if never_submitted.is_selected(): never_submitted.click()
      time.sleep(1)
      continue
    
    choice = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, attemp)))
    if not choice.is_selected(): choice.click()

  print('{:78s}{:5s}{:4s}'.format("6.  In 'Attemps that are: just leave 'Never Submitted', 'Finished' unchecked, the rest are checked","  -  ","Done"))
  # In 'Attemps that are: just leave 'Never Submitted', 'Finished' unchecked, the rest are checked - End

  #  Click 'Show report' - Begin
  show_report = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'id_submitbutton')))
  show_report.click()

  print('{:78s}{:5s}{:4s}'.format("7.  Click 'Show report'","  -  ","Done"))
  #  Click 'Show report' - End

  # Confirm the quiz's results are shown - Begin
  time.sleep(2)
  assert "You must select at least one state." not in self.driver.page_source

  print('{:78s}{:5s}{:4s}'.format("8.  Confirm the quiz's results are shown","  -  ","Done"))
  # Confirm the quiz's results are shown - End
  

  



class MoodleTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_VIEW_QUIZ_RESULT_4(self):
    print('\n')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('If the test resulted in any errors, this is because of the incorrect timing of the appearance the elements of the page.\nPlease run the test 1-2 more times')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('\n')

    """
    The steps of this test are as followed:
    1.  Login as manager
    2.  Go to a predetermined course
    3.  Turn on Edit Mode
    4.  Click 'Module 1 quick check'
    5.  Click 'Results'
    6.  In 'Attemps that are: just leave 'Never Submitted', 'Finished' unchecked, the rest are checked
    7.  Click 'Enable' in 'Time limit'
    8.  Confirm the quiz's results are shown
    """

    login(self)
    view_quiz_result(self)
  
  def tearDown(self):
    time.sleep(2)
    self.driver.quit()
    # pass
  
if __name__ == "__main__":
  unittest.main()