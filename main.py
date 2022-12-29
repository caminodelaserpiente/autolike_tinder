import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class Web_Scraping_pgn(unittest.TestCase):

    def setUp(self):
        # Conf path downloads files
        path_diver = "./chromedriver"
        service = Service(executable_path=path_diver)

        options = Options()
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument('user-data-dir=/home/gnu/github/autolike_tinder/chromedb')

        self.driver= webdriver.Chrome(service=service, options=options)
        driver = self.driver

        url = "https://www.tinder.com"
        driver.get(url)
        time.sleep(3)


    def test_like(self):
        driver = self.driver

        for i in range (60):
            # auto like
            like_button = driver.find_element(By.XPATH, '//button//span[text()="Like"]')
            driver.execute_script("arguments[0].click();", like_button)
            time.sleep(.36)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'web_scraping'))
