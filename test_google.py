from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. Заходим на Вики
driver.get("https://ru.wikipedia.org")

# 2. Ищем поле поиска.
# На Вики у него обычно name="search" или ID "searchInput"
search_input = driver.find_element(By.NAME, "search")
search_input.send_keys("Python")

# 3. А вот и твоя находка! Кликаем по кнопке с name="go"
search_button = driver.find_element(By.NAME, "go")
search_button.click()

# 4. Дадим секунду подгрузиться и проверим заголовок
time.sleep(2)
assert "Python" in driver.title

print("Тест Википедии пройден!")
driver.quit()
