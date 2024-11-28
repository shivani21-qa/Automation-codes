from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()


# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# Wait for the page to load (you may also use WebDriverWait for better handling)
time.sleep(2)

# Locate the username and password fields
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# Enter the login credentials (default demo credentials)
username = "Admin"
password = "admin123"

username_field.send_keys(username)
password_field.send_keys(password)

# Locate and click the login button
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

# Wait for a few seconds to let the page load after login
time.sleep(5)

# Optional: Verify if login was successful by checking the page title or URL
if "dashboard" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")
# Close the browser

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button').click()
time.sleep(5)
screenshot_path= "shivani_file.png"
driver.save_screenshot(screenshot_path)
driver.quit()
