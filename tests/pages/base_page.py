class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, *args):
        return self.browser.find_element(*args)

    def find_elements_texts(self, *args):
        return self.browser.find_elements(*args)