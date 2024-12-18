from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    usr = "" 
    pwd = ""

    driver = None

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://www.facebook.com/')
    print("Opened Facebook")

    driver.find_element(By.NAME, "email").send_keys(usr)
    print("Email Id entered")
    sleep(1)

    driver.find_element(By.NAME, "pass").send_keys(pwd)
    print("Password entered")

    driver.find_element(By.NAME, "login").click()

    sleep(10)

except Exception as e:
    print("The error raised is: ", e)

finally:
    if 'driver' in locals() and driver is not None:
        driver.quit()
        print("Driver quit successfully.")
