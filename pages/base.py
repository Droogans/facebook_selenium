from selenium import webdriver


class BasePage(object):
    webdriver = webdriver.Firefox()

    def go(self):
        self.webdriver.get(self.url)
