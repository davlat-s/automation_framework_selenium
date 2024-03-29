from selenium import webdriver
from selenium.webdriver.common.by import By

name_textbox_id = 'name'
email_textbox_id = 'email'
phone_textbox_id = 'phone'
adress_textarea_id = 'textarea'

class LeftPage():

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, input):
        id = name_textbox_id
        self.driver.find_element(By.ID, id).clear()
        self.driver.find_element(By.ID, id).send_keys(input)
    
    def set_email(self, input):
        id = email_textbox_id
        self.driver.find_element(By.ID, id).clear()
        self.driver.find_element(By.ID, id).send_keys(input)

    def set_phone(self, input):
        id = phone_textbox_id
        self.driver.find_element(By.ID, id).clear()
        self.driver.find_element(By.ID, id).send_keys(input)
    
    def set_adress(self, input):
        id = adress_textarea_id
        self.driver.find_element(By.ID, id).clear()
        self.driver.find_element(By.ID, id).send_keys(input)

    def get_name(self):
        id = name_textbox_id
        return self.driver.find_element(By.ID, id).get_attribute("value")

    def get_email(self):
        id = email_textbox_id
        return self.driver.find_element(By.ID, id).get_attribute("value")

    def get_phone(self):
        id = phone_textbox_id
        return self.driver.find_element(By.ID, id).get_attribute("value")
    
    def get_adress(self):
        id = adress_textarea_id
        return self.driver.find_element(By.ID, id).get_attribute("value")

    