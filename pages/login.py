from selenium.webdriver.common.keys import Keys as K


class FacebookLogin(object):

    def __init__(self, webdriver):
        self.webdriver = webdriver
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
    def retrieve_friend_requests_button(self):
        """
        retrieves name by partial href
        """
        return self.webdriver.find_element_by_name('requests')

    @property
    def retrieve_private_messages_button(self):
        """
        retrieves private messages button info
        """
        return self.webdriver.find_element_by_name('mercurymessages')

    @property
    def retrieve_notifications_button(self):
        return self.webdriver.find_element_by_name('notifications')

    def login(self):
        """
        fills email and password fields,
        then clicks enter
        """
        self.retrieve_email_field.send_keys('')  # Enter your facebook email
        self.retrieve_password_field.send_keys('')  # Enter your facebook password
        self.retrieve_password_field.send_keys(K.RETURN)

    def click_requests(self):
        """
        clicks requests button
        to show friend requests
        """
        self.retrieve_friend_requests_button.click()

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