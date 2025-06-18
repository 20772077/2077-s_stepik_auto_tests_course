from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 
    #ссылки для тестов
    link = "http://suninjuly.github.io/selects1.html" #выполняется успешно
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    x1 = browser.find_element(By.ID, "num1")
    #x = x1.text
    x2 = browser.find_element(By.ID, "num2")

    res = int(x1.text)+int(x2.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()