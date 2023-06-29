#!/usr/bin/env python3

"""
Project to test HTML5 Solitaire Mahjong game
"""

import os
import logging
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class CustomTestResult(unittest.TextTestResult):
    def getDescription(self, test):
        # Get the test description
        desc = super().getDescription(test)
        # Remove the test class name from the description
        return  desc.replace(' (__main__.TestMajongGame)', '')

    def addSuccess(self, test):
        self.stream.write("OK\n")

    def startTest(self, test):
        # Print a separator line before each test case
        self.stream.writeln('-' * 40)
        super().startTest(test)

class CustomTextTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        # Override the method to use the custom test result class
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

    def get_test_order(self, suite):
        # Define the desired order of test execution
        test_order = [
            "test_verify_title",
            "test_menu_elements_existence",
            "test_menu_elements_layout",
            "test_menu_buttons_color_properties",
            "test_menu_elements_dimension_properties",
            "test_menu_elements_hover",
            "test_menu_elements_navigation",
            "test_start_background",
            "test_start_board_elements_existence",
            "test_start_board_elements_position",
            "test_start_board_elements_size",
            "test_start_board_elements_layout",
            "test_start_board_elements_navigation",
            "test_game_elements_position",
            "test_game_elements_size",
            "test_game_elements_navigation",
            "test_game_elements_existence",
            "test_game_elements_layout",
            "test_mahjong_game_move",
            "test_mahjong_game_match_tiles",
            "test_mahjong_game_undo",
            "test_mahjong_game_load_hints",
            "test_mahjong_game_lose_game",
            "test_mahjong_game_clear_board",
            "test_mahjong_game_modify_theme",
        ]

        # Sort the test cases based on the desired order
        sorted_tests = sorted(suite, key=lambda x: test_order.index(x._testMethodName))
        return sorted_tests

    def run(self, suite):
        # Get the sorted order of tests
        sorted_tests = self.get_test_order(suite)

        # Create a new suite with the sorted tests
        sorted_suite = unittest.TestSuite(sorted_tests)

        # Run the tests in the desired order
        print("Starting tests...")
        return super().run(sorted_suite)

class TestMajongGame(unittest.TestCase):

    @classmethod
    def get_options(cls):
        options = Options()
        return options

    @classmethod
    def setUpClass(cls):
        """ Set up Selenium WebDriver w/ Firefox GeckoDriver"""

        # Load environment variables
        cls.website_url = os.environ.get('WEBSITE_URL')

        # Load environment variables
        cls.website_driver = os.environ.get('WEB_DRIVER')

        # Load environment variables
        cls.driver_log = os.environ.get('DRIVER_LOG_PATH')

        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger(__file__)

        # Check if the environment variable is set
        if cls.website_url is None or cls.website_driver is None:
            assert False, "environment variables are not set."
            exit()

        cls.options = cls.get_options()
        cls.logger.debug("Before initializing driver")
        cls.driver = webdriver.Firefox(service=Service(cls.website_driver, log_path=cls.driver_log), options=cls.options)
        cls.logger.debug("After initializing driver")

    @classmethod
    def tearDownClass(cls):
        """ Close the browser window after all tests run"""
        cls.driver.quit()
        cls.driver.service.log_file.close()
        cls.driver.service.stop()

    def setUp(self):
        """Get location of hosted game"""
        self.driver.get(self.website_url)

    def zoom(self, zoom_value):
        self.driver.execute_script(f"document.body.style.zoom='{zoom_value}%'")

    def test_verify_title():
        pass

    def test_menu_elements_existence():
        pass

    def test_menu_elements_layout():
        pass

    def test_menu_buttons_color_properties():
        pass

    def test_menu_elements_dimension_properties():
        pass

    def test_menu_elements_hover():
        pass

    def test_menu_elements_navigation():
        pass

    def test_start_background():
        pass

    def test_start_board_elements_existence():
        pass

    def test_start_board_elements_position():
        pass

    def test_start_board_elements_size():
        pass

    def test_start_board_elements_layout():
        pass

    def test_start_board_elements_navigation():
        pass

    def test_game_elements_position():
        pass

    def test_game_elements_size():
        pass

    def test_game_elements_navigation():
        pass

    def test_game_elements_existence():
        pass

    def test_game_elements_layout():
        pass

    def test_mahjong_game_move():
        pass

    def test_mahjong_game_match_tiles():
        pass

    def test_mahjong_game_undo():
        pass

    def test_mahjong_game_load_hints():
        pass

    def test_mahjong_game_lose_game():
        pass

    def test_mahjong_game_clear_board():
        pass

    def test_mahjong_game_modify_theme():
        pass

if __name__ == "__main__":
    """ Run set of unit tests """

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMajongGame)

    # Create an instance of the custom test runner
    runner = CustomTextTestRunner(verbosity=2, buffer=True)

    # Run the tests using the custom test runner
    runner.run(suite)
