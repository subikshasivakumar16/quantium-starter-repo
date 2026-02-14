from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Automatically downloads the correct ChromeDriver
service = Service(ChromeDriverManager().install())

# Start Chrome browser
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")

# Example: search for something
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello Selenium!")
search_box.submit()

# Wait a few seconds to see results
import time
time.sleep(5)

# Close the browser
driver.quit()
