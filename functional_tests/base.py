from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        opts = webdriver.chrome.options.Options()
        opts.add_argument('--headless')
        self.browser = webdriver.Chrome(options=opts)
        #self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def assert_row_in_list_table(self, row_text):     
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        assert row_text in [row.text for row in rows]

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
