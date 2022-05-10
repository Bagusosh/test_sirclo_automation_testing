import os
import platform
import warnings

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from loguru import logger


class WebViewDriver:

    def __init__(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        if platform.system() == "Darwin":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER"))

        # Data
        self.web_url = "http://qa-interview.srcli.xyz"
        self.valid_web_title = 'Welcome!'

        # xPaths
        self.title_text_xpath = "/html/body/h1"

        # Menu View Driver
        self.driver.maximize_window()

        self.driver.get(self.web_url)

        try:
            _ = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.XPATH, self.title_text_xpath), self.valid_web_title)
            )
        except TimeoutException:
            logger.error("Web doesn't exist")
            return
