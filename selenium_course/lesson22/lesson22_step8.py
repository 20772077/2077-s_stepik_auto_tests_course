from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    inputFirstName = browser.find_element(By.NAME, "firstname")
    inputFirstName.send_keys("Mad")
    inputLastname = browser.find_element(By.NAME, "lastname")
    inputLastname.send_keys("Jack")
    inputEmail = browser.find_element(By.NAME, "email")
    inputEmail.send_keys("mj1@gmail.com")

    inputFile = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')
    inputFile.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла