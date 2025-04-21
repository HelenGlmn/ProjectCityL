import time
import allure
import pytest
from selenium import webdriver
from pages.main_page import Main_page
from pages.product_card import Product_card_page
from pages.approve_page import Approve_page
from pages.basket_page import Basket_page


@pytest.mark.order(3)
@allure.description("Test 1")
def test_1(set_group):
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Start Test 1")

    mp = Main_page(driver)
    pc = Product_card_page(driver)
    ap = Approve_page(driver)
    bp = Basket_page(driver)

    mp.select_city()  # выбор города
    mp.set_value_search()  # вводим слова поиска Стиральные машины
    mp.select_popular_button()  # выбираем с сушкой (из попьюла боттон)
    mp.input_price_filter()  # вводим стоимость в фильтр - мин/макс
    mp.select_shop_filter_link()  # открытие ссылки Забрать в конкретном магазине
    mp.set_checkbox_city_filter()  # активируем чекбокс с названием магазина
    mp.set_checkbox_zab5min()  # активируем ченкбокс Забрать через 5 мин
    driver.execute_script("window.scrollBy(0, 700);")  # двигаем скролл вниз
    mp.click_radiobutton_5percent()  # активируем чекбокс ссылка 5%
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, 2000);")  # двигаем скролл вниз
    time.sleep(15)
    mp.select_button_apply_filter()  # нажимаем кнопку Применить фильтр
    time.sleep(15)
    mp.select_product_name_price()  # выводим название и цену товара
    mp.go_product_card()  # нажимаем ссылку Название продукта и переходим в карточку продукта
    time.sleep(15)
    pc.select_full_name_product()  # выводим полное название продукта
    print(f"цена с гл стр value_price(): {mp.value_price}")
    print(f"цена с карт товара pc.get_product_price_pc(): {pc.get_product_price_pc()}")

    # проверяем название продукта/стоимости в гл страницы и карточки товара
    assert mp.value_price == pc.get_product_price_pc(), f"Цена не совпадает: {mp.value_price} != {pc.get_product_price_pc()}"
    print('Цена товара совпадает')

    assert mp.product_name == pc.get_product_name_pc(), f"Название продукта не совпадает: {mp.product_name} != {pc.product_name_pc()}"
    print('Названия продуктов совпадает')

    pc.add_product_basket()  # нажимаем кнопку Оформить заказ
    ap.select_product_added_world()
    ap.select_name_product()
    ap.select_product_price()

    # проверяем название продукта с главной страницы и старницы Карточка товара
    assert mp.value_price == ap.find_product_price(), f"Цена не совпадает: {mp.value_price} != {ap.find_product_price()}"
    print('Цена товара совпадает')

    assert mp.product_name == ap.set_name_product(), f"Название продукта не совпадает: {mp.product_name} != {ap.set_name_product()}"
    print('Названия продуктов совпадает')

    ap.select_button_go_basket()  # нажать кнопку Оформить заказ

    bp.select_world()  # проверка слова Корзина
    bp.select_product_name()  # вывод названия продукта
    bp.select_product_price()  # вывод стоимости

    # проверяем название продукта и стоимость на главной странице и старнице Basket(Корзина

    assert mp.value_price == bp.value_product_price, f"Цена не совпадает: {mp.value_price} != {bp.value_product_price}"
    print('Цена товара совпадает')

    assert mp.product_name == bp.value_name_product, f"Название продукта не совпадает: {mp.product_name} != {bp.value_name_product}"
    print('Названия продуктов совпадает')

    bp.click_button_finish()  # нажимаем кнопку Перейти к оформлению
    bp.select_finish_word()  # проверяем на popwindow сообщение Зарегистрируйтесь или войдите в свой аккаунт,
    # чтобы получить баллы за покупку

    time.sleep(30)
    print("Finish Test 1")
    time.sleep(30)
    driver.quit()
