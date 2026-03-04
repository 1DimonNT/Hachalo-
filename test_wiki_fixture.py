from wiki_page import WikiPage


# def test_wiki_search_clean(browser):
#     # browser подтянется из conftest.py автоматически по имени
#     page = WikiPage(browser)
#
#     page.open()
#     page.search_for("Pytest")
def test_wiki_english_search(browser):
    # Создаем английскую вики с ожиданием 5 секунд
    page = WikiPage(browser, timeout=5, language="en")

    page.open()  # Откроет en.wikipedia.org
    page.search_for("Python")


    header_text = page.get_main_header_text()
    assert "python" in header_text.lower()  # Теперь совпадет!


