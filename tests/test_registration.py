import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

user_name = 'filipp_aslapov_19_001'
user_email = 'filipp_aslapov_19_018@mail.ru'
user_pass_succes_reg = 'Pass123'
user_pass_less_6_char = 'pas'

def test_successful_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(By.NAME, 'name').send_keys(user_name)
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(user_pass_succes_reg)

    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

    time.sleep(1)
    assert "login" in driver.current_url, f"Ожидался URL, содержащий '/login', но был {driver.current_url}"

def test_password_contains_less_than_6_characters(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(By.NAME, 'name').send_keys(user_name)
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(user_pass_less_6_char)

    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

    error_message = driver.find_element(By.CLASS_NAME, 'input__error').text
    assert "Некорректный пароль" in error_message, f"Ожидалось сообщение об ошибке 'Некорректный пароль', но было: {error_message}"
