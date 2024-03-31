
import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from selenium import webdriver
from time import sleep
from pageObjects.leftWelcomePage import LeftPage as LP
from selenium.webdriver.support.ui import WebDriverWait
from testCases.conftest import driver_setup
from datetime import datetime
from configurations import config
from utilities.customLogger import LogGen

logger = LogGen.loggen()
URL = config.URL    

class TestLeftPage:
    NAME = config.NAME
    EMAIL = config.EMAIL
    PHONE = config.PHONE
    ADDRESS = config.ADDRESS


    def test_welcome_page(self, driver_setup):
        logger.info("@@@@@@@@@@@ verifying welcome page @@@@@@@@@@@")
        self.driver = driver_setup
        self.driver.get(URL)
        actual_title = self.driver.title
        if actual_title == "Automation Testing Practice":
            self.driver.close()
            logger.info("welcome page passed")
            assert True
        else:
            now = datetime.now()
            self.driver.save_screenshot(f"./screenshots/test_welcome_page_{now}.png")
            self.driver.close()
            logger.error("welcome page failed")
            assert False

    def test_name(self, driver_setup):
        logger.info("@@@@@@@@@@@ verifying name textbox @@@@@@@@@@@")
        self.driver = driver_setup
        self.driver.get(URL)
        LP.set_name(self, self.NAME)
        sleep(2)
        result = LP.get_name(self)
        if result == self.NAME:
            self.driver.close()
            logger.info("name textbox passed")
            assert True
        else:
            now = datetime.now()
            self.driver.save_screenshot(f"./screenshots/test_name_{now}.png")
            self.driver.close()
            logger.error("name textbox failed")
            assert False

    def test_email(self, driver_setup):
        logger.info("@@@@@@@@@@@ verifying email textbox @@@@@@@@@@@")
        self.driver = driver_setup
        self.driver.get(URL)
        LP.set_email(self, self.EMAIL)
        sleep(2)
        result = LP.get_email(self)
        if result == self.EMAIL:
            self.driver.close()
            logger.info("email textbox passed")
            assert True
        else:
            now = datetime.now()
            self.driver.save_screenshot(f"./screenshots/test_email_{now}.png")
            self.driver.close()
            logger.error("email textbox failed")
            assert False

    def test_phone(self, driver_setup):
        logger.info("@@@@@@@@@@@ verifying phone textbox @@@@@@@@@@@")
        self.driver = driver_setup
        self.driver.get(URL)
        LP.set_phone(self, self.PHONE)
        sleep(2)
        result = LP.get_phone(self)
        if result == self.PHONE:
            self.driver.close()
            logger.info("phone textbox passed")
            assert True
        else:
            now = datetime.now()
            self.driver.save_screenshot(f"./screenshots/test_phone_{now}.png")
            self.driver.close()
            logger.error("phone textbox failed")
            assert False

    def test_address(self, driver_setup):
        logger.info("@@@@@@@@@@@ verifying address textarea @@@@@@@@@@@")
        self.driver = driver_setup
        self.driver.get(URL)
        LP.set_adress(self, self.ADDRESS)
        sleep(2)
        result = LP.get_adress(self)
        if result == self.ADDRESS:
            self.driver.close()
            logger.info("address textarea passed")
            assert True
        else:
            now = datetime.now()
            self.driver.save_screenshot(f"./screenshots/test_address_{now}.png")
            self.driver.close()
            logger.error("address textarea failed")
            assert False