from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersQaPage(BasePage):
    # Button of 'See all QA Jobs' locator.
    SEE_ALL_QA_JOBS_BUTTON_LOCATOR = (By.LINK_TEXT,
                                      "See all QA jobs")

    QA_HEADER_LOCATOR = (By.XPATH, "//h1[normalize-space()='Quality Assurance']")


    def go_to_careers_qa_page(self):
        """ Go to URL in below. """
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        print("Opened the URL in above.")

    def click_to_see_all_qa_jobs_button(self):
        """ Clicks to 'See all QA Jobs button. '"""
        self.wait_for_1_seconds()
        self.click_element(*self.SEE_ALL_QA_JOBS_BUTTON_LOCATOR)
        print("Clicked to 'See all QA Jobs' button.")


