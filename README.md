pytest-language-tests

Автотесты для проверки корректного отображения интерфейса интернет‑магазина на разных языках.

Что внутри

conftest.py — добавляет CLI‑опцию --language и поднимает Chrome c нужной локалью (intl.accept_languages).

test_items.py — одиночный тест, который открывает карточку товара и убеждается, что на странице есть кнопка «Добавить в корзину».

Быстрый старт

# клонируем репозиторий
git clone https://github.com/<ваш‑логин>/pytest-language-tests.git
cd pytest-language-tests

# создаём виртуальное окружение
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# устанавливаем зависимости
pip install -r requirements.txt

# запускаем тест (пример: испанский интерфейс)
pytest -v --language=es

Проверка переводаПри запуске с --language=fr тест делает паузу 30 секунд. В это время убедитесь, что на кнопке написано «Ajouter au panier».

Параметры CLI

Параметр

Описание

Значение по умолчанию

--language=<code>

Двухбуквенный ISO 639‑1 код локали браузера (en, ru, es, fr, …)

en

Требования

Python 3.8+

Google Chrome и совместимый chromedriver (проверьте chromedriver --version)

Пакеты из requirements.txt (Selenium ≥4, PyTest ≥7)

Структура репозитория

.
├── conftest.py
├── test_items.py

Как это работает

Опция --language считывается в pytest_addoption.

В фикстуре browser создаётся экземпляр webdriver.Chrome c преференсом intl.accept_languages.

Тест переходит по адресуhttp://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

Находит кнопку button.btn-add-to-basket и убеждается, что элемент присутствует и видим.

Полезные команды

# Headless‑режим (через дополнительный опциональный аргумент в conftest)
pytest -v --language=ru -o addopts="--headless"

# Формирование отчёта в JUnit‑формате
pytest --language=de --junitxml=report.xml

Лицензия

MIT

