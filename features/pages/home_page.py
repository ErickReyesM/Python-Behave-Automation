from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def write_on_class_example_input(self, word):
        text_input = self.driver.find_element(By.ID, 'autocomplete')
        text_input.clear()
        text_input.send_keys(word)

    def select_country_from_the_available_list(self, country):
        country_list_xpath = "//ul[@id='ui-id-1']//div[contains(text(),'{0}')]".format(country)
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(self.driver, timeout=3, poll_frequency=1, ignored_exceptions=errors)
        wait.until(lambda d: visibility_of(self.driver.find_element(By.XPATH, country_list_xpath)) or True)
        available_country = self.driver.find_element(By.XPATH, country_list_xpath)
        available_country.click()

    def click_on_the_dropdown(self):
        dropdown = self.driver.find_element(By.ID, 'dropdown-class-example')
        dropdown.click()

    def select_option_from_the_dropdown(self, option):
        option_xpath = "//select[@id='dropdown-class-example']//option[contains(text(),'{0}')]".format(option)
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(self.driver, timeout=3, poll_frequency=1, ignored_exceptions=errors)
        wait.until(lambda d: visibility_of(self.driver.find_element(By.XPATH, option_xpath)) or True)
        option = self.driver.find_element(By.XPATH, option_xpath)
        option.click()

    def open_new_window(self):
        open_window_button = self.driver.find_element(By.ID, 'openwindow')
        open_window_button.click()
        sleep(1)


