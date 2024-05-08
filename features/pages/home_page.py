from selenium.webdriver.common.by import By


class HomePage:
    search_bar_locator = 'mainSearchbar'
    suggested_articles_locator = 'm-typeahead'

    def __init__(self, driver):
        self.driver = driver

    def search_article(self, article):
        search_bar = self.driver.find_element(By.ID, self.search_bar_locator)
        search_bar.clear()
        search_bar.send_keys(article)

    def suggestion_displayed(self):
        suggested_articles = self.driver.find_element(By.CLASS_NAME, self.suggested_articles_locator)
        return suggested_articles.is_displayed()

