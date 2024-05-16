from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    search_bar_locator = 'mainSearchbar'
    suggested_articles_locator = "div.m-sayt-padd label"
    option_locator = ''

    def __init__(self, driver):
        self.driver = driver

    def search_article(self, article):
        search_bar = self.driver.find_element(By.ID, self.search_bar_locator)
        search_bar.clear()
        search_bar.send_keys(article)

    def suggestion_displayed(self):
        suggested_articles = (WebDriverWait(self.driver, 3)
                              .until(lambda x: x.find_elements(By.CSS_SELECTOR, self.suggested_articles_locator)))
        articles_text = [article.text for article in suggested_articles]
        return articles_text

    def click_on_option(self, option):
        self.option_locator = f"//ul[@class='row p-2 sayt-child']//li//p[contains(text(),'{option}')]"
        option_element = (WebDriverWait(self.driver, 3)
                          .until(lambda x: x.find_element(By.XPATH, self.option_locator)))
        option_element.click()

