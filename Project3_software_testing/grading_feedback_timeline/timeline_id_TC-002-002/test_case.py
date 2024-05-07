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

        dashboard = driver.find_element(By.LINK_TEXT, "Dashboard")
        time.sleep(2)
        dashboard.click()

        time.sleep(2)
        dayfilter = driver.find_element(By.ID, "timeline-day-filter-current-selection")
        time.sleep(2)
        dayfilter.click()

        time.sleep(2)
        day = driver.find_element(By.LINK_TEXT, "Next 30 days")
        time.sleep(2)
        day.click()

        time.sleep(2)
        viewilter = driver.find_element(By.ID, "timeline-view-selector-current-selection")
        time.sleep(2)
        viewilter.click()

        time.sleep(2)
        view = driver.find_element(By.LINK_TEXT, "Sort by dates")
        time.sleep(2)
        view.click()

        time.sleep(5)
        self.assertTrue("No activities require action" in self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)