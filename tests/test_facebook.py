import unittest
from selenium import webdriver
from pages.login import FacebookLogin


class TestFacebookLogin(unittest.TestCase):

    def setUp(self):
        self.webdriver = webdriver.Firefox()
        self.facebook_page = FacebookLogin(self.webdriver)
        self.facebook_page.webdriver.get(self.facebook_page.url)

    def test_login(self):
        """
        if logged in, there is a button
        for friend requests with name='requests'
        """
        self.facebook_page.login()
        self.assertIsNotNone(self.facebook_page.webdriver.find_element_by_name('requests'))

    def test_click_requests(self):
        self.test_login()
        self.facebook_page.click_requests()
        self.assertIsNotNone(self.facebook_page.webdriver.find_elements_by_class_name('hideToggler'))

    def test_click_private_messages(self):
        self.test_login()
        self.facebook_page.click_private_messages()
        self.assertIsNotNone(self.facebook_page.webdriver.find_elements_by_class_name('hideToggler'))

    def test_click_notifications(self):
        self.test_login()
        self.facebook_page.click_notifications()
        self.assertIsNotNone(self.facebook_page.webdriver.find_elements_by_class_name('hideToggler'))

    def tearDown(self):
        self.webdriver.close()

if __name__ == '__main__':
    unittest.main()