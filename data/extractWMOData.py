#### Extractiing Data From WMO ####
### Auther :Layla Arnold
### Date : 2023-09-18
####################################

######  Importing Libraries ###
# Allows you to launch and initialize various web browsers like Chrome, Firefox, etc.
from selenium import webdriver
# Provides a way to configure and manage the ChromeDriver instance.
from selenium.webdriver.chrome.service import Service
# Allows customization of Chrome WebDriver behavior, such as adding command-line options to the browser.
from selenium.webdriver.chrome.options import Options
# Helps in automatic management (download, install, update) of the ChromeDriver binary.
from webdriver_manager.chrome import ChromeDriverManager
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def openChrome(link):
    # Options customize Chrome WebDriver behavior
    options = Options()

    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Navigate to the desired URL
    driver.get(link)

    # wait for page to load
    wait = WebDriverWait(driver, 60)
    return driver, wait

link = "https://app.powerbi.com/view?r=eyJrIjoiZjNhNzIzM2YtMjRkYS00ZjJjLWEzZmMtNmQzMGQzMDdiODU3IiwidCI6ImVhYTZiZTU0LTQ2ODctNDBjNC05ODI3LWMwNDRiZDhlOGQzYyIsImMiOjl9"
driver_instance , wait = openChrome(link)


