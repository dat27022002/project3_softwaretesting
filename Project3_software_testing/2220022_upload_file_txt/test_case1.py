"""
Tester: Nguyen Viet Minh Tan
MSSV: 2220022
Test feature: Upload File
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
  print('{:67s}{:5s}{:4s}'.format("Login as manager","  -  ","Done"))


def upload_file(self):
  # Turn on Edit Mode - Begin
  self.driver.get("https://school.moodledemo.net/course/view.php?id=27")
  time.sleep(2)

  edit_mode_btn = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "custom-control-input"))
  ).click()

  print('{:67s}{:5s}{:4s}'.format("Edit Mode turned ON","  -  ","Done"))
  print("\n")
  time.sleep(4)
  assert "Edit course" in self.driver.title
  # Turn on Edit Mode - End

  useful_resources = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "coursecontentcollapse1"))
  )
  useful_resources.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/div[3]/div/section/div/div/div/ul/li[2]/div[1]/div[2]/div[2]/div/button").click()
  print('{:67s}{:5s}{:4s}'.format("Press 'Add an activity or resource'","  -  ","Done"))

  upload_file_option = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "File"))
  ).click()
  print('{:67s}{:5s}{:4s}'.format("Choose 'File' in the pop-up window","  -  ","Done"))

  assert "New File" in self.driver.title

  elem = WebDriverWait(self.driver, 7).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'fp-btn-add'))
  )
  time.sleep(10)
  elem.find_element(By.TAG_NAME, 'a').click()

  print('{:67s}{:5s}{:4s}'.format("Press the button to add new file","  -  ","Done"))

  # Upload file interactable section
  WebDriverWait(self.driver, 7).until(
    EC.presence_of_element_located((By.NAME, 'repo_upload_file'))
  ).send_keys("C:\\Users\\Admin\\Desktop\\selenium\\upload_file.txt")
  print('{:67s}{:5s}{:4s}'.format("Upload file from local system","  -  ","Done"))

  # Submit file to be uploaded button
  WebDriverWait(self.driver, 7).until(
    EC.presence_of_element_located((By.XPATH, "//button[text() = 'Upload this file']"))
  ).click()
  print('{:67s}{:5s}{:4s}'.format("Click the 'Upload this file' to submit the uploaded file","  -  ","Done"))
  time.sleep(3)

  name = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_name"))
  )

  save_return_btn = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_submitbutton2"))
  )

  name.click()
  name.clear()
  name.send_keys("test-upload-file")
  print('{:67s}{:5s}{:4s}'.format("Fill in the 'Name' input box with the required name of the new file","  -  ","Done"))
  

  save_return_btn.click()
  print('{:67s}{:5s}{:4s}'.format("Click the 'Save and return to course'","  -  ","Done"))

  uploaded_file = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "test-upload-file"))
  )

  assert "test-upload-file" in self.driver.page_source
  print("\n")
  print('{:67s}{:5s}{:4s}'.format("Confirm that new file has been added to the course","  -  ","Done"))



class MoodleTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_UPLOAD_FILE(self):
    print('\n')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('If the test resulted in any errors, this is because of the incorrect timing of the appearance the elements of the page.\nPlease run the test 1-2 more times')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('\n')

    """
    The steps of this test are as followed:
    1.  Login as manager
    2.  Turn on Edit Mode
    3.  Press any of the "Add an activity or resource
    4.  Choose 'File' in the pop-up window
    5.  Press the button to add new file
    6.  Upload file from local system
    7.  Click the 'Upload this file' to submit the uploaded file
    8.  Fill in the 'Name' input box with the required name of the new file
    9.  Click the 'Save and return to course'
    10. Confirm that new file has been added to the course
    """

    login(self)
    upload_file(self)
  
  def tearDown(self):
    time.sleep(2)
    self.driver.quit()
  
if __name__ == "__main__":
  unittest.main()