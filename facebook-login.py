from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    usr = "bludgeon0@gmail.com" 
    pwd = "Taivnqq12"

    driver = None

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://erp.e-mongolia.mn/login')

    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Нэвтрэх нэр']")
    username_field.send_keys(usr)   
    sleep(1)

    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Нууц үг']")
    password_field.send_keys(pwd)
    print("Password entered")

    login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'el-button enterButton') and span[text()='Нэвтрэх']]")
    login_button.click()
    sleep(10)

except Exception as e:
    print("The error raised is: ", e)

finally:
    if 'driver' in locals() and driver is not None:
        sleep(12)
        driver.quit()
        print("Driver quit successfully.")
