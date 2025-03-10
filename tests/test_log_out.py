import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

user_email = 'filipp_aslapov_19_015@mail.ru'
user_pass_succes_reg = 'Pass123'

def test_log_out_of_your_account(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(user_pass_succes_reg)

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Выход']").click()
    time.sleep(3)

    header = driver.find_element(By.XPATH, "//h2[text()='Вход']")
    assert header.text == 'Вход', f"Ожидался текст 'Вход', но был {header.text}"




