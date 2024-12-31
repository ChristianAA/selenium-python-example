from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from guara.transaction import AbstractTransaction
from data.locators import SearchPageLocators
from selenium.webdriver.support.wait import WebDriverWait


class Search(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = SearchPageLocators
        self.wait = WebDriverWait(self._driver, 10)

    def do(self, for_text):
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.locator.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(for_text)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.locator.SEARCH_BUTTON)
        )
        search_button.click()

        self.wait.until(EC.presence_of_all_elements_located(self.locator.RESULTS))
        return self._driver.find_element(By.CSS_SELECTOR, ".SnptgjT2zdOhGYfNng6g").text
