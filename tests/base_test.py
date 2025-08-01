import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    #Base (Home Page) URL of 'Insider' company.
    base_url = 'https://useinsider.com/'
    #Careers page URL of 'Insider' company.
    careers_url = 'https://useinsider.com/careers/'
    #Careers > Quality Assurance page URL of 'Insider' company.
    careers_qa_url = 'https://useinsider.com/careers/quality-assurance/'
    #Careers > Open Positions > Department = 'Quality Assurance' URL of 'Insider' company.
    careers_open_positions_qa_url = 'https://useinsider.com/careers/quality-assurance/'


    def setUp(self):
        chrome_options = Options()
        """ Disable notifications comes from browser. """
        chrome_options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(chrome_options)
        """ Maximizes (full-screen) driver. """
        self.driver.maximize_window()
        """ Gets URL from base_url. """
        self.driver.get(self.base_url)
        """ Continue searching for a specified period of time (Max. 10 Seconds)"""
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """ Close the driver. """
        self.driver.quit()