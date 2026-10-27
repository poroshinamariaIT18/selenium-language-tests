import time


def test_guest_can_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Обязательное условие задания: пауза 30 секунд для визуальной проверки рецензентом
    time.sleep(30)

    # Ищем кнопку добавления в корзину по уникальному CSS-селектору
    # Селектор 'button.btn-add-to-basket' уникален для этой страницы
    add_to_basket_button = browser.find_element("css selector", "button.btn-add-to-basket")

    # Проверяем, что элемент существует и виден на странице
    assert add_to_basket_button.is_displayed(), "Кнопка добавления в корзину не найдена или не видна"

    # (Опционально) Выводим текст кнопки в консоль для наглядности
    print(f"\nButton text is: '{add_to_basket_button.text}'")