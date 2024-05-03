import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        service = webdriver.ChromeService(executable_path = PATH)
        self.driver = webdriver.Chrome(service=service)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org1")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)