import unittest
import warnings

from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from driver.view import WebViewDriver


class EndpointTests(unittest.TestCase):
    def setUp(self) -> None:
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = WebViewDriver().driver

        # data
        self.error_message = 'Page not found'

        self.error_url = "http://qa-interview.srcli.xyz/regist"

        # xpath
        self.error_message_xpath = '/html/body/pre'



    def test_invalid_endpoint(self):
        with self.driver as driver:
            self.driver.get(self.error_url)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.error_message_xpath), self.error_message)
                )
            except TimeoutException:
                logger.error('Check invalid endpoint error')

            assert self.error_message in driver.page_source
            logger.success('Check invalid endpoint success')

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_invalid_endpoint'))
        return test_suite