from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as econ
from selenium.webdriver.support.wait import WebDriverWait
from webConfig import WebDrivers
from variables import buur


class TraineeManagement:
    def __init__(self):
        self.web = WebDrivers("SM")
        self.wait = WebDriverWait(self.web.driver, 50)

    def login(self):
        self.web.driver.get(buur.lamp_page)
        self.wait.until(econ.visibility_of_element_located((By.XPATH, buur.landing_login)))
        self.click_an_element(buur.landing_login)
        self.insert_a_value(buur.email_field, buur.login_email)
        self.insert_a_value(buur.password_field, buur.Login_password)
        self.click_an_element(buur.login_button)
        self.wait.until(econ.visibility_of_element_located((By.XPATH, buur.invite_button)))

    def invite_trainee(self):
        self.click_an_element(buur.invite_button)
        self.click_an_element(buur.email_field2)
        self.insert_a_value(buur.email_field2, buur.employees_email)
        self.click_an_element(buur.add_button)
        self.click_an_element(buur.send_invite_button)
        self.click_an_element(buur.close_button)

    def create_group(self):
        self.click_an_element(buur.Trainees_tab)
        self.click_an_element(buur.groups_tab)
        self.click_an_element(buur.create_button)
        self.click_an_element(buur.group_field)
        self.click_an_element(buur.others)
        self.click_an_element(buur.group_field)
        self.insert_a_value(buur.groups_name_field , buur.groups_name)
        self.click_an_element(buur.assign_course_field)
        self.click_an_element(buur.course_name)
        self.click_an_element(buur.create_group_button)

    def click_an_element(self, field):
        self.web.driver.find_element_by_xpath(field).click()
        self.web.driver.implicitly_wait(50)

    def insert_a_value(self, field, value):
        self.web.driver.find_element_by_xpath(field).send_keys(value)

    def verify(self, element, word):
        validate = self.web.driver.find_element_by_xpath(element)
        try:
            assert word == validate.text
            print("successful")
        except AssertionError:
            print("Not found")
