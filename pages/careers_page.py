from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    # Header of 'Locations' section.
    LOCATIONS_SECTION_HEADER_LOCATOR = (By.XPATH,
                                        "//h3[contains(text(), 'Our Locations')]")
    # Button of 'Teams' section.
    TEAMS_SECTION_BUTTON_LOCATOR = (By.LINK_TEXT,
                                    "See all teams")
    # Header of 'Life at Insider' section locator.
    LIFE_AT_INSIDER_SECTION_HEADER_LOCATOR = (By.XPATH,
                                              "//h2[text()='Life at Insider']")

    def scroll_to_locations_section(self):
        """ Scrolls to 'Locations' section. """
        self.wait_for_1_seconds()
        self.scroll_to_section(self.LOCATIONS_SECTION_HEADER_LOCATOR)
        print("Scrolled to 'Locations' section.")

    def scroll_to_teams_section(self):
        """ Scrolls to 'Teams' section. """
        self.wait_for_1_seconds()
        self.scroll_to_section(self.TEAMS_SECTION_BUTTON_LOCATOR)
        print("Scrolled to 'Teams' section.")

    def scroll_to_life_at_insider_section(self):
        """ Scrolls to 'Life at Insider' section. """
        self.wait_for_1_seconds()
        self.scroll_to_section(self.LIFE_AT_INSIDER_SECTION_HEADER_LOCATOR)
        print("Scrolled to 'Life at Insider' section.")
