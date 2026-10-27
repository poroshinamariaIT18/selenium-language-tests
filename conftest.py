import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Добавляем опцию командной строки --language
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language for browser'
    )


@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение языка из командной строки
    language = request.config.getoption("language")

    # Настраиваем опции браузера Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print(f"\nStart browser for test with language: {language}...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser...")
    browser.quit()


# Этот хук не обязателен для теста, но он помогает выводить выбранный язык в итоговом отчете pytest.
def pytest_terminal_summary(terminalreporter):
    lang = terminalreporter.config.getoption("language")
    print(f"\nTests were run with language: {lang}")