from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_is_there(browser):
    browser.get(link)
    time.sleep(3) # небольшая пауза для проверки надписи на кнопке для тестировщика
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) > 0, "Кнопка не найдена"
    