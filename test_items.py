import time
from selenium.webdriver.common.by import By

# Товар, указанный в условии задания
PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    """Проверяем наличие кнопки добавления товара в корзину на странице продукта."""
    browser.get(PRODUCT_LINK)

    # Нам нужно 30 секунд, чтобы вручную убедиться в правильности перевода кнопки
    time.sleep(30)

    add_btn = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert (
        add_btn and add_btn[0].is_displayed()
    ), "Кнопка добавления в корзину не найдена на странице товара"
