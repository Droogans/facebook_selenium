from selenium.webdriver.common.keys import Keys

from config import secrets

from pages.base import BasePage


class FacebookLogin(BasePage):

    def __init__(self):
        self.webdriver = BasePage.webdriver
        self.url = 'http://facebook.com'

    @property
    def retrieve_email_field(self):
        """
        retrieves email field on facebook
        login page
        """
        return self.webdriver.find_element_by_name('email')

    @property
    def retrieve_password_field(self):
        """
        retrieves password field on facebook
        login page
        """
        return self.webdriver.find_element_by_name('pass')

    @property
    def retrieve_private_messages_button(self):
        """
        retrieves private messages button info
        """
        return self.webdriver.find_element_by_name('mercurymessages')

    @property
    def retrieve_notifications_button(self):
        return self.webdriver.find_element_by_name('notifications')

    def login(self, username=None, password=None):
        """
        fills email and password fields,
        then clicks enter
        """
        username = username or secrets.username
        password = password or secrets.password
        self.retrieve_email_field.send_keys(username)
        self.retrieve_password_field.send_keys(password)
        self.retrieve_password_field.send_keys(Keys.RETURN)

    def click_private_messages(self):
        """
        clicks requests button
        to show private messages
        """
        self.retrieve_private_messages_button.click()

    def click_notifications(self):
        """
        clicks requests button
        to show friend requests
        """
        self.retrieve_notifications_button.click()
