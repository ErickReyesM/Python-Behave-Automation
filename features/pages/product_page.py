from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    product_title_locator = 'h1'
    product_price_locator = 'm-product__price-dw-promotion'

    def __init__(self, driver):
        self.driver = driver

    def product_title_displayed(self):
        product_title = (WebDriverWait(self.driver, 3)
                         .until(lambda x: x.find_element(By.TAG_NAME, self.product_title_locator)))
        return product_title.is_displayed()

    def product_price_displayed(self):
        product_price = (WebDriverWait(self.driver, 3)
                         .until(lambda x: x.find_element(By.CLASS_NAME, self.product_price_locator)))
        return product_price.is_displayed()
