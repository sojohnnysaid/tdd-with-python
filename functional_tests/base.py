from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_WAIT = 5

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        opts = webdriver.chrome.options.Options()
        opts.add_argument('--headless')
        self.browser = webdriver.Chrome(options=opts)
        #self.browser = webdriver.Firefox()

        self.By = By
        self.wait = WebDriverWait(self.browser, 10)
        self.expect = EC

    def tearDown(self):
        self.browser.quit()

    def assert_row_in_list_table(self, row_text):     
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        assert row_text in [row.text for row in rows]
