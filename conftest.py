import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\n--- Запуск браузера через conftest ---")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\n--- Закрытие браузера ---")
    driver.quit()
