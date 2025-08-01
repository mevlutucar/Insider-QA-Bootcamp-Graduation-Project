from pages.careers_open_positions_page import CareersOpenPositionsPage
from pages.careers_page import CareersPage
from pages.careers_qa_page import CareersQaPage
from pages.home_page import HomePage
from tests.base_test import BaseTest

"""
Reproduce Steps
1. Open "https://useinsider.com/" URL.
2. Verify that the Insider homepage leads successfully.
3. Click on the “Company” menu in the navigation bar.
4. Click on “Careers” from the dropdown.
5. Verify that the Careers page is loaded by confirming the presence of 
"Locations", "Teams", and "Life at Insider" sections.
6. Open "https://useinsider.com/careers/quality-assurance/" URL.
7. Click on the “See all QA jobs” button.
8. On the job listings page, apply the Location filter as “Istanbul, Turkiye”.
9. On the job listings page, apply the Department filter as “Quality Assurance.”
10. Verify that job postings are listed.
11. For each listed job posting, validate:
    • The position title contains “Quality Assurance”
    • The department is “Quality Assurance”
    • The location is “Istanbul, Turkiye”
12. Click on the “View Role” button of first job listing.
13. Confirm that it redirects to the Lever application page.

"""

""" This Selenium Python project made by Mevlut Ucar. """

class TestCheckFilterAndListQaJobs(BaseTest):
    def test_check_insider_filter_and_list_qa_jobs(self):
#------------------------------- beginning of home_page ---------------------------------------------------------------
        home_page = HomePage(self.driver)
        self.driver.implicitly_wait(5)
        """ Verify base_url matches with current_url """
        self.assertEqual(self.base_url, home_page.get_current_url(), "You are not in 'Home' page!")

        if home_page.is_element_present(*home_page.CLOSE_POPUP_BUTTON_LOCATOR):
            home_page.close_the_popup_button()
            """ Verify Popup shows and closes or if it doesn't show, skip this step and continue. """
            self.assertFalse(home_page.is_element_present(*home_page.CLOSE_POPUP_BUTTON_LOCATOR),
                             "Popup is not closed!")
        else:
            print("Popup not found. Skipping popup close step.")

        home_page.accept_the_cookie_button()
        """ Verify 'Cookie' visibles and accepts on page. """
        self.assertTrue(home_page.is_element_visible(*home_page.ACCEPT_COOKIE_BUTTON_LOCATOR),
                         "Cookie is not accepted!")

        home_page.hover_to_company_category_dropdown_menu()
        """ Verify 'Careers' sub menu visibles on page. """
        self.assertTrue(home_page.is_element_visible(*home_page.CATEGORY_CAREERS_LOCATOR),
                        "'Careers' sub menu is not visible!")

        home_page.click_to_careers_category_sub_menu()
        """ Verify 'Find your calling' text presents on page. """
        self.assertTrue(home_page.is_text_present("Find your calling"),
                        "'Careers' page not loaded correctly!")
#------------------------------- end of home_page ---------------------------------------------------------------------

#------------------------------ beginning of careers_page -------------------------------------------------------------
        careers_page = CareersPage(self.driver)
        """ Verify 'Find your calling' text presents on page. """
        self.assertTrue(careers_page.is_text_present("Find your calling"),
                        "'Careers' page not loaded correctly!")

        careers_page.scroll_to_locations_section()
        """ Verify 'Our Locations' text presents on page. """
        self.assertTrue(careers_page.is_text_present("Our Locations"),
                        "'Location' section not found!")

        careers_page.scroll_to_teams_section()
        """ Verify 'See all teams' text presents on page. """
        self.assertTrue(careers_page.is_text_present("See all teams"),
                        "'Teams' section not found!")

        careers_page.scroll_to_life_at_insider_section()
        """ Verify 'Life at Insider' text presents on page. """
        self.assertTrue(careers_page.is_text_present("Life at Insider"),
                        "'Life at Insider' section not found!")
#------------------------------ end of careers_page -------------------------------------------------------------------

#------------------------------ beginning of careers_qa_page ----------------------------------------------------------
        careers_qa_page = CareersQaPage(self.driver)
        careers_qa_page.go_to_careers_qa_page()
        """ Verify 'Q&A team' text presents on page. """
        self.assertTrue(careers_page.is_text_present("Q&A team"),
            "'Q&A team' text is not present on the 'Quality Assurance' page!")

        """ Verify 'See all QA jobs' button visibles """
        self.assertTrue(careers_qa_page.is_element_visible(*careers_qa_page.SEE_ALL_QA_JOBS_BUTTON_LOCATOR),
                        "'See all QA jobs' button is not visible!")
        careers_qa_page.click_to_see_all_qa_jobs_button()
#------------------------------ end of careers_qa_page ----------------------------------------------------------------

#------------------------------ beginning of careers_open_positions_page ----------------------------------------------
        careers_open_positions_page = CareersOpenPositionsPage(self.driver)
        """ Verify 'Open Positions' text presents on page. """
        self.assertTrue(careers_open_positions_page.is_text_present("Open Positions"),
            "'Open Positions' text is not present on the 'Open Positions' page!")

        careers_open_positions_page.click_to_location_dropdown_menu()
        """ Verify 'Filter by Location' text presents on page. """
        self.assertTrue(careers_open_positions_page.is_text_present("Filter by Location"),
            "'Filter by Location' text is not present on the 'Open Positions' page!")

        careers_open_positions_page.click_to_department_dropdown_menu()
        """ Verify 'Filter by Department' text presents on page. """
        self.assertTrue(careers_open_positions_page.is_text_present("Filter by Department"),
            "'Filter by Department' text is not present on the 'Open Positions' page!")

        careers_open_positions_page.scroll_hover_and_click_to_view_role_button()
        """ Verify 'View Role' button visibles on page. """
        self.assertTrue(careers_open_positions_page.is_element_visible
                        (*careers_open_positions_page.FIRST_VIEW_ROLE_BUTTON_LOCATOR),
                        "'View Role' button is not visible!")

        job_cards = careers_open_positions_page.get_all_job_cards()
        """ Verify existing jobs on page or show message. """
        self.assertGreater(len(job_cards), 0, "There is no jobs available!")

        for index, job in enumerate(job_cards, start=1):
            details = careers_open_positions_page.extract_job_details(job)

            print(f"\nJob {index} details: {details}")
            """ Verify 'title' value matches with 'Quality Assurance'. """
            self.assertIn("Quality Assurance", details["title"],
                          f"Job {index} title does not contain 'Quality Assurance'")
            """ Verify 'department' value matches with 'Quality Assurance'. """
            self.assertEqual(details["department"], "Quality Assurance",
                             f"Job {index} department is not 'Quality Assurance'")
            """ Verify 'location' value matches with 'Istanbul, Turkiye'. """
            self.assertIn(details["location"], ["Istanbul, Turkiye"],
                          f"Job {index} location is not 'Istanbul, Turkiye'")

        careers_open_positions_page.switch_to_lever_job_application_tab_and_wait_5_secs()
        """ Verify this job redirects to jobs.lever.co website. """
        self.assertIn("jobs.lever.co", self.driver.current_url,
                      f"Not redirected to Lever: {self.driver.current_url}")
#------------------------------ end of careers_open_positions_page ----------------------------------------------------

