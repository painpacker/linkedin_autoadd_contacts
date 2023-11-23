from selenium import webdriver
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(5)
email_address_form = ("")
password_form = ("")
actions = ActionChains(driver)

def submit_form():
    sign_in = driver.find_element(By.CLASS_NAME, "main__sign-in-link")
    sign_in.click()

    driver.refresh()

    email = driver.find_element(By.ID, "username")
    email.click()
    email.send_keys(email_address_form)

    password = driver.find_element(By.ID, "password")
    password.click()
    password.send_keys(password_form)

    submit = driver.find_element(By.CLASS_NAME, "login__form_action_container ")
    submit.click()
    time.sleep(15)


submit_form()


def open_users():
    driver.maximize_window()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'msg-overlay-bubble-header__control') and contains(@class, 'msg-overlay-bubble-header__control--new-convo-btn')]")))
    buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'msg-overlay-bubble-header__control') and contains(@class, 'msg-overlay-bubble-header__control--new-convo-btn')]")
    if len(buttons) >= 2:
        hide = buttons[1]
        actions.move_to_element(hide).click().perform()
        time.sleep(5)
    all_users = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button') and contains(@class, 'artdeco-button--muted') and contains(@class, 'artdeco-button--2') and contains(@class, 'artdeco-button--tertiary') and contains(@class, 'ember-view') and contains(@class, 'ph2')]//*[text()='См. все']")
    actions.move_to_element(all_users).click().perform()
    time.sleep(5)


open_users()


def add_users():
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                         "//button[contains(@class, 'artdeco-button') and contains(@class, 'artdeco-button--2') and contains(@class, 'artdeco-button--secondary') and contains(@class, 'ember-view') and contains(@class, 'full-width')]")))

    scrollable_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "artdeco-modal__content.discover-cohort-recommendations-modal__content"))
    )

    index = 0
    while True:
        try:
            buttons = driver.find_elements(By.XPATH,
                                           "//button[contains(@class, 'artdeco-button') and contains(@class, 'artdeco-button--2') and contains(@class, 'artdeco-button--secondary') and contains(@class, 'ember-view') and contains(@class, 'full-width')]")
            for i in range(index, index + 4):
                try:
                    button = buttons[i]
                    actions = ActionChains(driver)
                    actions.move_to_element(button).click().perform()
                    time.sleep(1)
                except IndexError:
                    break
            index += 4
            driver.execute_script("arguments[0].scrollTop += 350;", scrollable_element)
            time.sleep(2)
        except:


add_users()
