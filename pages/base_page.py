from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, *locator):
        """Finds and returns a web element using the provided locator."""
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        """Clicks on the web element specified by the given locator."""
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        """Hovers on the web element specified by the given locator."""
        element = self.find(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        """Returns active page current URL on the web element"""
        return self.driver.current_url

    def wait_element(self, method, message: ''):
        """Waits until the specified element is clickable"""
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        """Retrieves the visible text of a web element after waiting for it to be clickable."""
        return self.wait_element(locator, "Element not found to get text.").text

    def scroll_to_section(self, locator):
        """ Scrolls the page to bring the specified element into view using ActionChains.
        This helps make elements visible before interacting with them. """
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

    def wait_for_15_seconds(self):
        """ Waits for 10 seconds """
        time.sleep(15)

    def wait_for_5_seconds(self):
        """ Waits for 5 seconds. """
        time.sleep(5)

    def wait_for_1_seconds(self):
        """ Waits for 1 second."""
        time.sleep(1)

    def wait_if_element_exists(self, locator, timeout=5):
        """
        Waits for an element to be clickable for 10 seconds.
        Returns the element if found, otherwise returns None.
        """
        try:
            short_wait = WebDriverWait(self.driver, timeout)
            return short_wait.until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            return None

    def wait_popup_element(self, locator):
        """
        Tries to close the popup if it appears.
        """
        popup = self.wait_if_element_exists(locator)
        if popup:
            popup.click()
            print("Closed the Popup.")
        else:
            print("Popup was not present. Continuing without closing.")

    def switch_to_lever_job_tab_and_wait_5_seconds(self):
        """ Switches to lever tab and waits for 5 seconds. """
        lever_url_prefix = "https://jobs.lever.co/"
        all_tabs = self.driver.window_handles

        for tab in all_tabs:
            self.driver.switch_to.window(tab)
            time.sleep(1)
            if self.driver.current_url.startswith(lever_url_prefix):
                print("Switched to Lever tab.")
                time.sleep(5)
                return

        raise Exception("Lever tab not found!")

    def is_element_present(self, *locator):
        """ Tries to find element that present. """
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def is_element_visible(self,*locator):
        """ Tries to find element that visible. """
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    def is_text_present(self, text):
        """ Tries to find text that visible. """
        return text in self.driver.page_source



