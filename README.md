# Selenium + PyTest Homework

Домаш­ние задания из курсового трека *«Автоматизация тестирования с помощью Selenium и PyTest»* (Stepik).  
Каждый модуль вынесен в отдельную папку, чтобы легче отслеживать прогресс и изменения.

---

## Содержание

| Модуль | Краткое описание | Ключевые файлы |
|--------|------------------|----------------|
| 01-selenium-intro | Первые шаги: поиск элементов, базовые проверки | `test_registration.py` |
| 02-pytest-basics  | Фикстуры, параметризация, xfail/skip          | `conftest.py`, `test_items.py` |
| 03-page-objects   | Реализация PATTERN Page Object               | `pages/base_page.py`, `pages/product_page.py` |
| 04-final-project  | Итоговый проект — автотесты интернет-магазина | `tests/test_basket.py`, `requirements.txt` |

---

## Быстрый старт

```bash
git clone https://github.com/<ваш-логин>/selenium-pytest-homework.git
cd selenium-pytest-homework
python -m venv venv
source venv/bin/activate        # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
pytest -q                       # запустить все тесты
