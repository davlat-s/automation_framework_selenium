import sys
from os.path import dirname, abspath

# setting up sys path
parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from selenium import webdriver
from time import sleep
from pageObjects.leftWelcomePage import LeftPage as LP
from pageObjects.rightWelcomePage import RightPage as RP
from selenium.webdriver.support.ui import WebDriverWait
from testCases.conftest import driver_setup
from datetime import datetime
from configurations import config
from utilities.customLogger import LogGen
from utilities.csv_reader import read_csv
from configurations import config


logger = LogGen.loggen()
URL = config.URL   

class TestRightPage():
    WIKIPEDIA_SEARCH_LIST = read_csv(config.CSV_PATH)

    def test_wiki_page_title(self, driver_setup):
        logger.info("@@@@@@@@@@@ testing wikipedia page titles @@@@@@@@@@@")
        self.driver = driver_setup
        self.driver.get(URL)
        self.driver.implicitly_wait(5)
        iterations = 0
        for s in self.WIKIPEDIA_SEARCH_LIST:
            RP.set_wikipedia_input_box(self, s)
            RP.click_search_button(self)
            RP.click_first_link(self)
            self.driver.switch_to.window(self.driver.window_handles[1])
            first_heading = RP.get_first_heading_text(self)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            logger.info(f"search: {s}, first heading: {first_heading}")
            if first_heading is not None:
                iterations += 1

        if iterations == len(self.WIKIPEDIA_SEARCH_LIST):
            self.driver.close()
            logger.info("test_get_wikipedia_first_heading passed")
            assert True
        else:
            self.driver.close()
            logger.error("test_get_wikipedia_first_heading failed")
            assert False

