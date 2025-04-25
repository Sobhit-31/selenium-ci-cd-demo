from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_wikipedia_search():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open Wikipedia and perform search
    driver.get("https://www.wikipedia.org")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Automation Testing", Keys.RETURN)

    # Wait for the page to load and check title
    WebDriverWait(driver, 10).until(EC.title_contains("Test automation"))
    print("Title contains 'Test automation'")

    # Check if search results are visible
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".search-result")))
    # print("Search results found")

    # # Verify the first result contains 'Automation' and click
    # first_result = driver.find_element(By.CSS_SELECTOR, ".search-result a")
    # assert "Automation" in first_result.text, "The first result doesn't contain 'Automation'"
    # first_result.click()

    # # Wait for new page and check the title
    # time.sleep(2)
    # assert "Automation Testing" in driver.title, "Page title doesn't contain 'Automation Testing'"

    driver.quit()

if __name__ == "__main__":
    test_wikipedia_search()
