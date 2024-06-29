from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import SearchPageLocators


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://duckduckgo.com/"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))

    def make_a_search(self, input_text):
        search_input = self.wait.until(EC.visibility_of_element_located(self.locator.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(input_text)

        search_button = self.wait.until(EC.element_to_be_clickable(self.locator.SEARCH_BUTTON))
        search_button.click()

        self.wait.until(EC.presence_of_all_elements_located(self.locator.RESULTS))
        self.driver.save_screenshot("results/results.png")
