from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_booking():
    # Setup the ChromeDriver using WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Navigate to the SecureTech website (replace with actual URL)
    driver.get("https://securetech-website.com")  # Replace with your SecureTech URL

    # Scroll to Services section
    services_section = driver.find_element(By.ID, "services")  # Assuming there's an ID 'services'
    driver.execute_script("arguments[0].scrollIntoView();", services_section)
    time.sleep(1)

    # Locate the "Book Now" button for a specific service
    book_button = driver.find_element(By.XPATH, "//button[contains(text(),'Service Name')]")  # Replace with actual service name
    book_button.click()
    time.sleep(1)

    # Accept the booking alert (assuming the alert pops up)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert Text: {alert_text}")
    alert.accept()

    # Quit the driver after the test is complete
    driver.quit()

if __name__ == "__main__":
    test_booking()
