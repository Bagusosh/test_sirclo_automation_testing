import unittest
import warnings

from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from faker import Faker

from driver.view import WebViewDriver


class DataTests(unittest.TestCase):
    def setUp(self) -> None:
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = WebViewDriver().driver

        # data
        fake = Faker('id-ID')
        self.error_message = 'Page not found'

        self.valid_username = 'root'
        self.valid_password = 'root123'
        self.valid_web_title = 'Welcome!'
        self.valid_data_page_title = 'Pemasukan'
        self.valid_timestamp_start = '2018-07-10'
        self.valid_timestamp_end = '2018-07-11'

        self.invalid_username = fake.first_name()
        self.invalid_password = fake.postcode()
        self.invalid_timestamp_start = '2018-07-11'
        self.invalid_timestamp_end = '2018-07-10'
        self.invalid_username = fake.first_name()
        self.invalid_password = fake.postcode()

        self.error_message_parameter_timestamp = 'Filter Parameter are wrong'

        self.login_url = "http://qa-interview.srcli.xyz/login"
        self.logout_url = "http://qa-interview.srcli.xyz/logout"
        self.data_url = "http://qa-interview.srcli.xyz/data"

        # xpath
        self.username_field_xpath = '/html/body/form/input[1]'
        self.password_field_xpath = '/html/body/form/input[2]'
        self.button_login_xpath = '/html/body/form/input[3]'
        self.title_text_xpath = "/html/body/h1"
        self.error_message_xpath = '/html/body/pre'
        self.data_page_tittle_xpath = '/html/body/h1[1]'
        self.timestamp_start_xpath = '/html/body/form/input[1]'
        self.timestamp_end_xpath = '/html/body/form/input[2]'
        self.button_submit_timestamp_xpath = '/html/body/form/input[3]'
        self.table_pemasukan_xpath = '/html/body/table[1]'
        self.table_pengeluaran_xpath = '/html/body/table[2]'


    def test_check_data_before_login(self):
        with self.driver as driver:
            self.driver.get(self.data_url)
            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))
                ).send_keys(self.valid_username)
            except TimeoutException:
                logger.error('Check data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))
                ).send_keys(self.valid_password)
            except TimeoutException:
                logger.error('Check data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
                ).click()
            except TimeoutException:
                logger.error('Check data error')

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.title_text_xpath), self.valid_web_title)
                )
            except TimeoutException:
                logger.error('Check data error')

            self.driver.get(self.data_url)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.data_page_tittle_xpath), self.valid_data_page_title)
                )
            except TimeoutException:
                logger.error('Check data error')

            assert self.valid_data_page_title in driver.page_source
            logger.success('Check data before login success')

    def test_check_data_after_login(self):
        with self.driver as driver:
            self.driver.get(self.login_url)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))
                ).send_keys(self.valid_username)
            except TimeoutException:
                logger.error('Check data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))
                ).send_keys(self.valid_password)
            except TimeoutException:
                logger.error('Check data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
                ).click()
            except TimeoutException:
                logger.error('Check data error')

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.title_text_xpath), self.valid_web_title)
                )
            except TimeoutException:
                logger.error('Check data error')

            self.driver.get(self.data_url)

            assert self.valid_data_page_title in driver.page_source
            logger.success('Check data after login success')

    def test_check_data_with_valid_timestamp(self):
        with self.driver as driver:
            self.driver.get(self.login_url)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))
                ).send_keys(self.valid_username)
            except TimeoutException:
                logger.error('Check data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))
                ).send_keys(self.valid_password)
            except TimeoutException:
                logger.error('Check data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
                ).click()
            except TimeoutException:
                logger.error('Check data error')

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.title_text_xpath), self.valid_web_title)
                )
            except TimeoutException:
                logger.error('Check data error')

            self.driver.get(self.data_url)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.timestamp_start_xpath))
                ).send_keys(self.valid_timestamp_start)
            except TimeoutException:
                logger.error('Check data error')

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.timestamp_end_xpath))
                ).send_keys(self.valid_timestamp_end)
            except TimeoutException:
                logger.error('Check data error')

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_submit_timestamp_xpath))
                ).click()
            except TimeoutException:
                logger.error('Check data error')

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.table_pemasukan_xpath)),
                    EC.visibility_of_element_located((By.XPATH, self.table_pengeluaran_xpath))
                )
                table_exist = True
            except TimeoutException:
                logger.error('Check data error')
                table_exist = False
                return

            assert table_exist is True
            logger.success('Check data with valid timestamp success')

    def test_check_data_with_invalid_timestamp(self):
        with self.driver as driver:
            with self.driver as driver:
                self.driver.get(self.login_url)

                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))
                    ).send_keys(self.valid_username)
                except TimeoutException:
                    logger.error('Check data error')
                    return

                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))
                    ).send_keys(self.valid_password)
                except TimeoutException:
                    logger.error('Check data error')
                    return

                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
                    ).click()
                except TimeoutException:
                    logger.error('Check data error')

                #after login
                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, self.title_text_xpath), self.valid_web_title)
                    )
                except TimeoutException:
                    logger.error('Check data error')

                self.driver.get(self.data_url)

                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, self.timestamp_start_xpath))
                    ).send_keys(self.invalid_timestamp_start)
                except TimeoutException:
                    logger.error('Check data error')

                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, self.timestamp_end_xpath))
                    ).send_keys(self.invalid_timestamp_end)
                except TimeoutException:
                    logger.error('Check data error')

                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, self.button_submit_timestamp_xpath))
                    ).click()
                except TimeoutException:
                    logger.error('Check data error')

                try:
                    _ = WebDriverWait(driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, self.error_message_xpath), self.error_message_parameter_timestamp)
                    )
                except TimeoutException:
                    logger.error('Check data error')

                assert self.error_message_parameter_timestamp in driver.page_source
                logger.success('Check data with invalid timestamp success')

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_check_data_before_login'))
        test_suite.addTest(cls('test_check_data_after_login'))
        test_suite.addTest(cls('test_check_data_with_valid_timestamp'))
        test_suite.addTest(cls('test_check_data_with_invalid_timestamp'))
        return test_suite

    def tearDown(self) -> None:
        pass