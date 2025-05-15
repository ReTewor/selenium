import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser: pytest.Parser) -> None:
    """Добавляем кастомный CLI‑параметр `--language` со значением по умолчанию `en`."""
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="UI language to test, e.g. ru, es, fr, ...",
    )


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest):
    """Запускаем Chrome c заданным языком интерфейса и отдаём драйвер в тест."""
    user_language: str = request.config.getoption("--language")

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    # При желании можно включить headless, но в учебном задании этого не требуется
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()
