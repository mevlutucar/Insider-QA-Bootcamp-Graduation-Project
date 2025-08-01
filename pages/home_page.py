import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    # Close '(x)' button locator on the pop-up on the top of right corner.
    CLOSE_POPUP_BUTTON_LOCATOR = (By.CLASS_NAME,
                                  "ins-close-button")
    # Accept button locator on cookie bar on the bottom of the website.
    ACCEPT_COOKIE_BUTTON_LOCATOR = (By.ID,
                                    "wt-cli-accept-all-btn")
    # Company dropdown menu locator on the navbar locator.
    CATEGORY_COMPANY_LOCATOR = (By.XPATH,
                                "(//a[@id='navbarDropdownMenuLink'])[5]")
    # Careers submenu locator shows when hover on category dropdown menu.
    CATEGORY_CAREERS_LOCATOR = (By.XPATH,
                                "//a[text()='Careers']")

    def close_the_popup_button(self):
        """ Clicks to close '(x)' button on the popup on the top of right corner. """
        self.wait_popup_element(self.CLOSE_POPUP_BUTTON_LOCATOR)

    def accept_the_cookie_button(self):
        """ Clicks to 'Accept All' button on the cookie bar on the bottom of the website. """
        self.click_element(*self.ACCEPT_COOKIE_BUTTON_LOCATOR)

    def hover_to_company_category_dropdown_menu(self):
        """ Hovers on 'Company' dropdown menu on the navbar. """
        self.hover_element(*self.CATEGORY_COMPANY_LOCATOR)
        print("Hovered to 'Company' dropdown menu on the navbar.")
        self.wait_for_1_seconds()

    def click_to_careers_category_sub_menu(self):
        """ Clicks to 'Careers' sub menu. """
        self.click_element(*self.CATEGORY_CAREERS_LOCATOR)
        print("Clicked to 'Careers' sub menu.")
