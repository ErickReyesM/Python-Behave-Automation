from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    size_more_link_locator = "a#Tamao"
    price_radiobutton_locator = "variants.prices.sortPrice-"
    brand_checkbox_locator = "brand-"
    result_products_locators = "ul.m-product__listingPlp li.m-product__card.card-masonry.a"

    def __init__(self, driver):
        self.driver = driver

    def show_more_sizes(self):
        more_sizes_link = (WebDriverWait(self.driver, 20)
                           .until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.size_more_link_locator))))
        more_sizes_link.click()

    def select_size(self, size):
        size_checkbox = (WebDriverWait(self.driver, 20)
                         .until(EC.element_to_be_clickable((By.ID, f"variants.normalizedSize-{size}"))))
        size_checkbox.click()

    def select_price(self, price):
        price_radiobutton = (WebDriverWait(self.driver, 20)
                             .until(EC.element_to_be_clickable((By.ID, self.price_radiobutton_locator + price))))
        price_radiobutton.click()

    def select_brand(self, brand):
        brand_checkbox = (WebDriverWait(self.driver, 20)
                          .until(EC.element_to_be_clickable((By.ID, self.brand_checkbox_locator + brand.upper()))))
        brand_checkbox.click()

    def products_displayed(self, brand):
        products = (WebDriverWait(self.driver, 20)
                    .until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.result_products_locators))))
        return len(products)
