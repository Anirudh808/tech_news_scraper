from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Configure logging for better feedback
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SeleniumDriver:
    def __init__(self):
        self.driver = None
        self.start_browser()

    def start_browser(self):
        """
        Starts a standard Chrome browser instance.
        """
        options = Options()
        # options.add_argument("detach", True)
        options.add_argument("--headless")    # Run Chrome in headless mode (no UI)
        # options.add_argument("--disable-gpu") # Often not needed with --headless in modern Chrome

        try:
            logging.info("Attempting to start Chrome browser...")
            self.driver = webdriver.Chrome(
                # executable_path=get_driver_manager().install(), # Use the global driver manager
                options=options
            )
            logging.info("Browser started successfully.")
        except Exception as e:
            logging.error(f"Error starting browser: {e}")
            if self.driver:
                self.driver.quit() # Ensure driver is closed if an error occurs

