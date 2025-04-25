from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Automation Testing with Python")
    search_box.submit()

    time.sleep(2)
    assert "Selenium" in driver.title
    driver.quit()
