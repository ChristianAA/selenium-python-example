from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='searchbox_homepage']//*[@type='submit']")
    RESULTS = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")
