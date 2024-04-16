from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def write_on_class_example_input(self, word):
        text_input = self.driver.find_element(By.ID, 'autocomplete')
        text_input.clear()
        text_input.send_keys(word)

    def select_country_from_the_available_list(self, country):
        country_list_xpath = "//ul[@id='ui-id-1']//div[contains(text(),'{0}')]".format(country)
        available_country = self.driver.find_element(By.XPATH, country_list_xpath)
        wait = WebDriverWait(self.driver, timeout=3)
        wait.until(lambda d: visibility_of(available_country))
        available_country.click()

    def click_on_the_dropdown(self):
        dropdown = self.driver.find_element(By.ID, 'dropdown-class-example')
        dropdown.click()

    def select_option_from_the_dropdown(self, option):
        option_xpath = "//select[@id='dropdown-class-example']//option[contains(text(),'{0}')]".format(option)
        option = self.driver.find_element(By.XPATH, option_xpath)
        wait = WebDriverWait(self.driver, timeout=3)
        wait.until(lambda d: visibility_of(option))
        option.click()


