# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Config import
from config import config

# Set up and start driver, returns a driver
def driver(withHomeDir, headless):
    # Set up Selenium
    mobile_emulation = {"deviceName": "Pixel 2"}  # Mobile emulation needed for story uploads

    # Add options
    chrome_options = webdriver.ChromeOptions()

    # Flag: Use data directory to save login data (for Instagram bot)
    if withHomeDir:
        chrome_options.add_argument("user-data-dir=selenium")

    #Unfortuantely, the file selection wizard requires some hacky headless browsing antics
    if headless:
        chrome_options.add_argument("--headless")

    #Mobile emulation required for story upload. No story upload feature for desktop site
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Start up driver
    return webdriver.Chrome(config['path_to_driver'], desired_capabilities=chrome_options.to_capabilities())