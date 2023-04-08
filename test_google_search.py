import pytest
from selene import browser
from selene import be, have
from selenium.webdriver.common.by import By


@pytest.fixture()
def precondition():
    browser.open('https://google.com')
    browser.driver.set_window_size(1280, 720)  # Setting window size
    if browser.driver.find_element(By.ID, 'L2AGLb').is_displayed():
        browser.driver.find_element(By.ID, 'L2AGLb').click()  # Accepting cookie
    yield
    browser.driver.quit()


def test_successful_search(precondition):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_unsuccessful_search(precondition):
    browser.element('[name="q"]').should(be.blank).type('ettestcteactce123123').press_enter()
    browser.element('[id="topstuff"]').should(have.text('- did not match any documents.'))
    print('Поиск не дал результатов')
