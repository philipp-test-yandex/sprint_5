import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

user_email = 'filipp_aslapov_19_011@mail.ru'
user_pass_succes_reg = 'Pass123'

def test_login_from_button_voity_v_account(driver):
    driver.get('https://stellarburgers.nomoreparties.site')

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(user_pass_succes_reg)

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")  # Используем правильный XPath для поля email
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email


# 2. Вход через кнопку «Личный кабинет»
def test_login_from_personal_account_button(driver):
    driver.get('https://stellarburgers.nomoreparties.site')

    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(user_pass_succes_reg)


    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")  # Используем правильный XPath для поля email
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email


# 3. Вход через кнопку в форме регистрации
def test_login_from_registration_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(user_pass_succes_reg)


    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")  # Используем правильный XPath для поля email
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email


# 4. Вход через кнопку в форме восстановления пароля
def test_login_from_password_recovery_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(user_pass_succes_reg)

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email