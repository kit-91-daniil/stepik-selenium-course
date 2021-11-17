import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


def time_result():
    answer = math.log(int(time.time()))
    return str(answer)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_calculate_time_result(browser, link):
    browser.get(link)
    textarea_field = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
    textarea_field.send_keys(time_result())
    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()

    result = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
    result_text = str(result.text)
    print(result_text)

    assert result_text == "Correct!"
