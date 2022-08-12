
from selenium.webdriver.common.by import By


class searchEngineResultPage:

    resultLinks = (By.CSS_SELECTOR, 'a.result__a')
    searhInput = (By.ID, 'search_form_input')


    def __init__(self,browser):
        self.browser = browser
        pass

    def result_link_titles(self):
        return[]

    def search_input_value(self):
        return ""

    def title(self):
        return ""