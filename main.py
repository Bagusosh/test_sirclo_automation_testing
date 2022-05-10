import os
import unittest

from loguru import logger
from tests.login.login import LoginTests
from tests.data.data import DataTests
from tests.endpoint.error_endpoint import EndpointTests

def suite():
    test_suite = unittest.TestSuite()

    LoginTests.as_suite(test_suite)
    DataTests.as_suite(test_suite)
    EndpointTests.as_suite(test_suite)

    return test_suite

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger.info(f"Starting {os.getcwd()}")
    runner = unittest.TextTestRunner(failfast=False)
    runner.run(suite())