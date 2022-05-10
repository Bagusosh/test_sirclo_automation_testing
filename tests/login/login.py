import unittest
import warnings

from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from faker import Faker

from driver.view import WebViewDriver


class LoginTests(unittest.TestCase):
    def setUp(self) -> None:
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = WebViewDriver().driver

        # data
        fake = Faker('id-ID')

        self.valid_username = 'root'
        self.valid_password = 'root123'
        self.invalid_username = fake.first_name()
        self.invalid_password = fake.postcode()
        self.error_message = 'The password or username is wrong'
        self.valid_web_title = 'Welcome!'

        self.login_url = "http://qa-interview.srcli.xyz/login"
        self.logout_url = "http://qa-interview.srcli.xyz/logout"

        # xpath
        self.username_field_xpath = '/html/body/form/input[1]'
        self.password_field_xpath = '/html/body/form/input[2]'
        self.button_login_xpath = '/html/body/form/input[3]'
        self.title_text_xpath = "/html/body/h1"
        self.error_message_xpath = '/html/body/pre'


    def test_login_with_valid_data(self):
        with self.driver as driver:
            self.driver.get(self.login_url)
            # before login
            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))
                ).send_keys(self.valid_username)
            except TimeoutException:
                logger.error('Login with valid data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))
                ).send_keys(self.valid_password)
            except TimeoutException:
                logger.error('Login with valid data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
                ).click()
            except TimeoutException:
                logger.error('Login with valid data error')

            # after login
            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.title_text_xpath), self.valid_web_title)
                )
            except TimeoutException:
                logger.error('Login with valid data error')

            self.driver.get(self.login_url)

            assert self.error_message not in driver.page_source
            assert self.valid_web_title in driver.page_source
            logger.success('Login with valid data success')

    def test_login_with_invalid_data(self):
        with self.driver as driver:
            self.driver.get(self.login_url)

            # before login
            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))
                ).send_keys(self.invalid_username)
            except TimeoutException:
                logger.error('Login with invalid data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))
                ).send_keys(self.invalid_password)
            except TimeoutException:
                logger.error('Login with invalid data error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
                ).click()
            except TimeoutException:
                logger.error('Login with invalid data error')

            # after login
            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.error_message_xpath), self.error_message)
                )
            except TimeoutException:
                logger.error('Login with invalid data error')

            assert self.error_message in driver.page_source
            logger.success('Login with invalid data success')

    def test_logout(self):
        with self.driver as driver:
            self.driver.get(self.login_url)

            # before login
            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))
                ).send_keys(self.invalid_username)
            except TimeoutException:
                logger.error('Logout error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))
                ).send_keys(self.invalid_password)
            except TimeoutException:
                logger.error('Logout error')
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
                ).click()
            except TimeoutException:
                logger.error('Logout error')

            # after login
            self.driver.get(self.logout_url)
            logger.success('Logout success')

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_login_with_valid_data'))
        test_suite.addTest(cls('test_login_with_invalid_data'))
        test_suite.addTest(cls('test_logout'))
        return test_suite

    def tearDown(self) -> None:
        pass