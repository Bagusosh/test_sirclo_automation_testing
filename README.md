# Test Sirclo Automation Testing

## Quick Start




This repository for the answer to technical tests is automation testing using Selenium Python

To run this project, you will require :

- Python 3.6+
- Windows (Chrome) or MacOS (Safari)

### Setup and Run

You would need some drivers to be added. Please
check the table below for references.

| Driver  | URL |
| ------------- | ------------- |
| Chrome  | https://sites.google.com/chromium.org/driver/  |
| Edge  | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/  |
| Firefox  | https://github.com/mozilla/geckodriver/releases  |
| Safari  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/  |

Once all is setup, run the command.

`python main.py`

## Development

To further develop unittest within this repository, build a new class with the following body.

```python
import unittest
import warnings
import platform

from loguru import logger
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from faker import Faker
from driver.view import WebViewDriver


class ExampleTests(unittest.TestCase):

    def setUp(self) -> None:
        # Declare your setup and configuration here
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        if platform.system() == "Darwin":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome("chromedriver.exe")

        # Data
        # Declare your required data for the test here

        # xPaths and Reference
        # Declare your xPaths and references here

        # Etc.
        self.context = {}

    def test_case_a(self):
        # Test Case A
        pass
    
    def test_case_b(self):
        # Test Case B
        pass
    
    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls("test_case_a"))
        test_suite.addTest(cls("test_case_b"))
        return test_suite
    
    def tearDown(self) -> None:
        # Declare your exit here
        pass
```

For more references, please check any other examples in this repository.

