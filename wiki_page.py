# В файле wiki_page.py в самом верху добавь импорты для ожидания:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # <--- Добавь это!


class WikiPage:
    def __init__(self, driver, timeout=10, language="ru"):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.lang = language

        # ОБНОВЛЯЕМ ЗДЕСЬ: используем класс, который ты нашел (точка в начале обязательна!)
        self.SEARCH_INPUT = (By.CSS_SELECTOR, ".cdx-text-input__input")

        # Этого локатора теперь достаточно для поиска и нажатия Enter

        # Локаторы остаются те же
        self.SEARCH_INPUT = (By.NAME, "search")
        self.FIRST_HEADING = (By.ID, "firstHeading")

    def open(self):
        # Теперь ссылка зависит от того, что мы передали в __init__
        self.driver.get(f"https://{self.lang}.wikipedia.org/")

    def search_for(self, text):
        # Ждем, пока поле (которое ты нашел) станет видимым
        search_field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        # Печатаем текст (например, "Python")
        search_field.send_keys(text)

        # Самый важный момент: отправляем нажатие клавиши Enter
        search_field.send_keys(Keys.ENTER)

    def get_main_header_text(self):
        return self.driver.find_element(*self.FIRST_HEADING).text
