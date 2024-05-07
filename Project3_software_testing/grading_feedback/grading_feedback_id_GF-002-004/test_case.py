import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from constant import COURSE_NAME, ASSIGNMENT_NAME

username_correct = "teacher"
password_correct = "moodle"
username_wrong = "teacher1"
password_wrong = "moodle1"


class Test_grading(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://moodle.org/demo")
        self.login()

    def login(self):
        driver = self.driver
        button_mount_orange_school = driver.find_element(By.LINK_TEXT, "Mount Orange School")
        button_mount_orange_school.click()

        self.assertTrue("Try Moodle in a real-school environment with ready-made accounts" in self.driver.page_source)
        button_login = driver.find_element(By.LINK_TEXT, "Log in")
        button_login.click()

        self.assertTrue("Lost password?" in self.driver.page_source)
        input_username = driver.find_element(By.NAME, "username")
        input_username.clear()
        input_username.send_keys("teacher")
        input_password = driver.find_element(By.NAME, "password")
        input_password.clear()
        input_password.send_keys("moodle")
        button_handle_login = driver.find_element(By.ID, "loginbtn")
        button_handle_login.click()

        self.assertTrue("Course overview" in self.driver.page_source)

    def test_edit_grade(self):
        driver = self.driver
        driver.implicitly_wait(10)

        course = driver.find_element(By.LINK_TEXT, COURSE_NAME)
        time.sleep(2)
        course.click()

        time.sleep(2)
        assignment = driver.find_element(By.LINK_TEXT, ASSIGNMENT_NAME)
        time.sleep(2)
        assignment.click()

        time.sleep(2)
        navigation = driver.find_element(By.LINK_TEXT, "Grade")
        time.sleep(2)
        navigation.click()

        time.sleep(2)
        input_feedback = driver.find_element(By.ID, "id_assignfeedbackcomments_editor")
        input_feedback.clear()
        input_feedback.send_keys("Good work")
        time.sleep(2)

        input_fullname = driver.find_element(By.NAME, "grade")
        input_fullname.clear()
        input_fullname.send_keys("50,7")
        button_save = driver.find_element(By.NAME, "savechanges")
        button_save.click()

        self.assertTrue("The grade provided could not be understood:" in self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)