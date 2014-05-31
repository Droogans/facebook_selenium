import unittest

from pages.home import FriendRequestsPage
from pages.home import HomePage
from pages.home import MessagesPage
from pages.home import NotificationsPage
from pages.login import FacebookLogin

friend_requests_page = FriendRequestsPage()
home_page = HomePage()
login_page = FacebookLogin()
messages_page = MessagesPage()
notifications_page = NotificationsPage()


def setUpModule():
    login_page.go()


def tearDownModule():
    login_page.logout()


class TestFacebookLogin(unittest.TestCase):

    def test_login_succeeds_with_valid_credentials(self):
        login_page.login()
        self.assertIsNotNone(home_page.lnk_requests)

    def test_login_fails_with_invalid_credentials(self):
        login_page.login('andrew.yurisich@gmail.com', 'notreal')
        self.assertEquals(login_page.invalid_login_message, 'Invalid username or password')

    def test_click_requests(self):
        login_page.click_requests()
        self.assertIsNotNone(login_page.webdriver.find_elements_by_class_name('hideToggler'))

    def test_click_private_messages(self):
        login_page.click_private_messages()
        self.assertIsNotNone(login_page.webdriver.find_elements_by_class_name('hideToggler'))

    def test_first_notification_is_from_mom(self):
        home_page.click_notifications()
        notification = notifications_page.expand()[0]
        self.assertEquals(notification.sender, 'Mom')
        self.assertIsNotNone(login_page.webdriver.find_elements_by_class_name('hideToggler'))

if __name__ == '__main__':
    unittest.main()
