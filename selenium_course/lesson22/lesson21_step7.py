from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    #ссылки для тестов
    link = "https://suninjuly.github.io/get_attribute.html" #выполняется успешно
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    robotCB = browser.find_element(By.ID, "robotCheckbox")
    robotCB.click()

    radioBtn = browser.find_element(By.ID, "robotsRule")
    radioBtn.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()