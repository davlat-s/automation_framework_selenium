from selenium import webdriver
from selenium.webdriver.common.by import By
import pageObjects.locators as locators

wikipedia_input_box_id = locators.wikipedia_input_box_id
wikipedia_search_button_class = locators.wikipedia_search_button_class
first_result_link_xpath = locators.first_result_link_xpath
page_title_class = locators.page_title_class

class RightPage():

    def __init__(self, driver):
        self.driver = driver

    def set_wikipedia_input_box(self, input):
        id = wikipedia_input_box_id
        wikipedia_input_box = self.driver.find_element(By.ID, id).clear()
        wikipedia_input_box = self.driver.find_element(By.ID, id).send_keys(input)

    def click_search_button(self):
        self.driver.find_element(By.CLASS_NAME, wikipedia_search_button_class).click()

    def click_first_link(self):
        self.driver.find_element(By.XPATH, first_result_link_xpath).click()

    def get_first_heading_text(self):
        return self.driver.find_element(By.CLASS_NAME, page_title_class).text
