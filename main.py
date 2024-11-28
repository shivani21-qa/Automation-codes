from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

# Open a website
driver.maximize_window()
driver.get("https://www.30minutesfix.com")
search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search your device.....']")

# Enter the search term "iPhone 15"
search_input.send_keys("iPhone 15")

# Locate and click the search button
search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "#root > div.css-8xc8u > main > section.d-flex.align-items-center.MuiBox-root.css-yuobo > div > div > div > div > div.MuiBox-root.css-1asaykn > div > div.MuiBox-root.css-12sloe3 > div > div > div:nth-child(1)").click()
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header[2]/div/div[2]/button[1]").click()
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div/div[2]").click()
time.sleep(10)
driver.quit()

