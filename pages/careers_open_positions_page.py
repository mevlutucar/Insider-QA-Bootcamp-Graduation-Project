from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersOpenPositionsPage(BasePage):
    # 'Filter by Location' dropdown menu locator.
    LOCATION_DROPDOWN_MENU_LOCATOR = (By.XPATH,
                                      "//span[@aria-labelledby='select2-filter-by-location-container']")

    # Selection of Location as 'Istanbul, Turkey' locator.
    LOCATION_ISTANBUL_SELECTION_LOCATOR = (By.XPATH,
                                           "//li[contains(text(),'Istanbul')]")
    # 'Filter by Department' dropdown menu locator
    DEPARTMENT_DROPDOWN_MENU_LOCATOR = (By.XPATH,
                                        "//span[@aria-labelledby='select2-filter-by-department-container']")

    # Selection of Department as 'Quality Assurance' locator.
    DEPARTMENT_QA_SELECTION_LOCATOR = (By.XPATH,
                                       "//li[contains(text(), 'Quality Assurance')]")
    # The first button that named 'View Role' of direct to Lever job application form page locator.
    FIRST_VIEW_ROLE_BUTTON_LOCATOR = (By.XPATH,
                                      "(//a[normalize-space()='View Role'])[1]")
    # List of available jobs locator.
    JOB_CARD_LOCATOR = (By.CSS_SELECTOR,
                        "#jobs-list .position-list-item")
    # Title of available jobs locator.
    JOB_TITLE_LOCATOR = (By.CSS_SELECTOR,
                         ".position-title")
    # Department of available jobs locator.
    JOB_DEPARTMENT_LOCATOR = (By.CSS_SELECTOR,
                              ".position-department")
    # Location of available jobs locator.
    JOB_LOCATION_LOCATOR = (By.CSS_SELECTOR,
                            ".position-location")

    def click_to_location_dropdown_menu(self):
        """ Waits for 15 seconds
         Clicks to 'Filter by Location' dropdown menu.
         Waits for 1 second
         and Selects 'Istanbul, Turkey'. """
        self.wait_for_15_seconds()
        self.click_element(*self.LOCATION_DROPDOWN_MENU_LOCATOR)
        print("Clicked to 'Filter by Location' Dropdown menu.")
        self.wait_for_1_seconds()
        self.click_element(*self.LOCATION_ISTANBUL_SELECTION_LOCATOR)
        print("Selected value as 'Istanbul, Turkiye' on 'Filter by Location' Dropdown menu.")

    def click_to_department_dropdown_menu(self):
        """ Waits for 5 seconds
        Clicks to 'Filter by Department' dropdown menu.
        Waits for 1 second
        and Selects 'Quality Assurance'. """
        self.wait_for_5_seconds()
        self.click_element(*self.DEPARTMENT_DROPDOWN_MENU_LOCATOR)
        self.wait_for_1_seconds()
        print("Clicked to 'Filter by Department' Dropdown menu.")
        self.click_element(*self.DEPARTMENT_QA_SELECTION_LOCATOR)
        print("Selected value as 'Quality Assurance' on'Filter by Department' Dropdown menu.")

    def scroll_hover_and_click_to_view_role_button(self):
        """ Scrolls to section
        Hovers to section
        Waits for 1 second
        and Clicks to 'View Role' button. """
        self.scroll_to_section(self.FIRST_VIEW_ROLE_BUTTON_LOCATOR)
        print("Scrolled to first job of the list.")
        self.hover_element(*self.FIRST_VIEW_ROLE_BUTTON_LOCATOR)
        print("Hovered to 'View role' button of the first job in the list.")
        self.wait_for_1_seconds()
        self.click_element(*self.FIRST_VIEW_ROLE_BUTTON_LOCATOR)
        print("Clicked to 'View role' button of the first job in the list.")

    def switch_to_lever_job_application_tab_and_wait_5_secs(self):
        """ Switches to Lever Job application tab
        and Waits for 5 seconds."""
        self.switch_to_lever_job_tab_and_wait_5_seconds()
        print("Switched to Lever QA Job Tab and waited for 5 seconds.")

    """ Finds available jobs in the list """
    def get_all_job_cards(self):
        return self.driver.find_elements(*self.JOB_CARD_LOCATOR)

    """Extracts available job details in the list"""
    def extract_job_details(self, job_element):
        title = job_element.find_element(*self.JOB_TITLE_LOCATOR).text
        department = job_element.find_element(*self.JOB_DEPARTMENT_LOCATOR).text
        location = job_element.find_element(*self.JOB_LOCATION_LOCATOR).text
        return {
            "title": title.strip(),
            "department": department.strip(),
            "location": location.strip()
        }
