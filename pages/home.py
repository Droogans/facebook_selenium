from pages.base import BasePage


class HomePage(BasePage):
    """
    This is where you end up by default after logging in.
    """
    def __init__(self):
        self.webdriver = BasePage.webdriver
        self.url = ''

    @property
    def btn_requests(self):
        """
        The button that takes you to your pending friend requests.
        """
        return self.webdriver.find_element_by_name('requests')

    def go_to_friend_requests(self):
        """
        Clicks requests button to show friend requests.
        """
        self.btn_requests.click()


class FriendRequestsPage(BasePage):
    """A list of your pending friend requests.

    Get here by clicking the icon in the top right corner of the home
    page that has a couple of people in it.
    """
    def __init__(self):
        self.webdriver = BasePage.webdriver
        self.url = ''




class MessagesPage(BasePage):
    """
    Private messages from other users.
    """
    def __init__(self):
        self.webdriver = BasePage.webdriver
        self.url = ''


class NotificationsPage(BasePage):
    """
    Stuff pops up here when people comment on your stuff, post new stuff, etc.
    """
    def __init__(self):
        self.webdriver = BasePage.webdriver
        self.url = ''

    @property
    def lnk_notifications(self):
        """The link you click to see your notifications"""
        return self.webdriver.find_element_by_css('.notifications')

    def tbl_notifications(self):
        """The html elements that make up notifications"""
        return self.webdriver.find_elements_by_css('div.notification-border')

    def expand(self):
        """Expand the notifications popup, and return an object representing them."""
        if self.is_collapsed:
            self.lnk_notifications.click()
            return [Notification(n) for n in self.tbl_notifications]

    def collapse(self):
        if self.is_expanded:
            self.lnk_notifications.click()

    def is_expanded(self):
        return len(self.webdriver.find_elements_by_css('.notification-display-box')) > 0

    def is_collapsed(self):
        return not self.is_expanded()


class Notification(object):
    """Parses and formats the notifications popup into an object"""

    def __init__(self, notification_element):
        self.notification_element = notification_element

    @property
    def lbl_sender(self):
        """Label element that contains the sender's name"""
        return self.notification_element.find_element_by_css('p span')

    @property
    def sender(self):
        return self.lbl_sender.get_text
