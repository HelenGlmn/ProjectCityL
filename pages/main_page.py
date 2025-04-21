
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

import allure

class Main_page(Base):
    url = "https://www.citilink.ru/"
    url_after_search = "https://www.citilink.ru/catalog/stiralnye-mashiny/"
    url_after_click_popular_button = "https://www.citilink.ru/catalog/stiralnye-mashiny-s-sushkoi/?ref=mainmenu_set"


    def __init__(self, driver):
        super().__init__(driver)
        self.value_price = None
        self.product_name = None
        self.driver = driver

    value_field_search = "стиральные машины"
    city_name = "Тюмень"
    value_price_filter_min = '41000'
    value_price_filter_max = '45000'

    # Locators

    catalog = "//a[@data-meta-name='DesktopHeaderFixed__catalog-menu']"
    search_field = "//input[@placeholder = 'Поиск по товарам']"
    menu_item = "//a[@title = 'Стиральные машины']"
    city_selector = "//button[@data-meta-name = 'CityChangeButton']"
    city_field_search = "//input[@name = 'search-city']"
    city_fined = "(//span[@class='app-catalog-1q0i7p4-Hightlight--StyledHighlight eerhlj90'])[2]"
    popular_button = ("//div[@data-meta-name='Popular_Selection']//a[@class ='app-catalog-14s4sql-Anchor--Anchor "
                      "e1136wl80'][3]//button[@data-meta-name = 'Popular_Selection_Button']")
    clean_button = "//a[@data-meta-name='FilterHeader__clear']"

    price_filter_min = ("//*[@id='__next']/div[1]/main/section/div[2]/div/div[3]/section/div["
                        "1]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/input[1]")

    price_filter_max = ("//*[@id='__next']/div[1]/main/section/div[2]/div/div[3]/section/div["
                        "1]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/input[2]")

    shop_filter_link = ("//*[@id='__next']/div[1]/main/section/div[2]/div/div[3]/section/div["
                        "1]/div/div/div/div/div/div/div[3]/div[2]/div[3]")

    main_word = "//*[@id='__next']/div[1]/main/section/div[1]/div[1]/div[2]/h1"

    checkbox_city_filter = "//div[@data-meta-value='Тюмень ТЦ Фаворит']"

    checkbox_zab5min = "//div[@data-meta-value='Забрать через 5 минут']"

    radiobutton_5percent = "//div[@data-meta-value = '5% и больше']"


    button_apply_filter = ("//*[@id='__next']/div[1]/main/section/div[2]/div/div[3]/section/div["
                           "1]/div/div/div/div/div/div/div[3]/div[2]/div[18]/button[1]")

    product_link = "//div[@data-meta-name='ProductVerticalSnippet']//a[@data-meta-name='Snippet__title']"
    price = ("//*[@id='__next']/div[1]/main/section/div[2]/div/div[3]/section/div[2]/div[2]/div/div/div/div[4]/div["
             "3]/button/span/div[2]/span/span/span[1]")
    # Getters

    def get_product_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_link)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_button_apply_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply_filter)))

    def get_radiobutton_5percent(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_5percent)))

    def get_checkbox_city_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_city_filter)))

    def get_checkbox_zab5min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_zab5min)))

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_city_selector(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_selector)))

    def get_city_field_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_field_search)))

    def get_city_fined(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_fined)))

    def get_popular_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popular_button)))

    def get_clean_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clean_button)))

    def get_price_filter_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter_min)))

    def get_price_filter_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter_max)))

    def get_shop_filter_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_filter_link)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action
    def click_product_link(self):
        self.get_product_link().click()
        print("Click Product link")

    def get_product_name(self):
        self.product_name = None
        self.product_name = (self.get_product_link().get_attribute('title'))
        print(f"Product name: {self.product_name}")
        return self.product_name

    def get_value_price(self):
        self.value_price = None
        self.value_price = (self.get_price().text.replace(" ", ""))
        print(f"Product price: {self.value_price}")
        return self.value_price

    def click_search_field(self):
        self.get_search_field().click()
        print("Click search field")

    def set_value_search_field(self):
        self.get_search_field().send_keys(self.value_field_search)
        self.get_search_field().send_keys(Keys.RETURN)
        print("Set value search field")

    def set_city_selector(self):
        self.get_city_selector().click()
        print("Click city selector")

    def send_city_selector(self):
        self.get_city_field_search().send_keys(self.city_name)
        print("Input city name")

    def click_city_fined(self):
        self.get_city_fined().click()
        print("Click city fined")

    def click_popular_button(self):
        self.get_popular_button().click()
        print("Click popular button")

    def click_clean_button(self):
        self.get_clean_button().click()
        print("Click clean button")

    def send_price_filter_min(self):
        self.get_price_filter_min().clear()
        self.get_price_filter_min().send_keys(self.value_price_filter_min)
        self.get_price_filter_min().send_keys(Keys.RETURN)
        print(self.get_price_filter_min().get_attribute('value'))
        print("Input price filter min")

    def send_price_filter_max(self):
        self.get_price_filter_max().clear()
        self.get_price_filter_max().send_keys(self.value_price_filter_max)
        self.get_price_filter_max().send_keys(Keys.RETURN)
        print(self.get_price_filter_max().get_attribute('value'))
        print("Input price filter max")

    def click_shop_filter_link(self):
        self.get_shop_filter_link().click()
        print("Click shop filter link")

    def click_get_button_apply_filter(self):
        self.get_button_apply_filter().click()
        print("Click button apply filter")

    def select_radiobutton_5percent(self):

        # Проверяем текущее состояние
        is_checked = self.get_radiobutton_5percent().is_selected()
        print(f"Текущее состояние радио баттона 5%: {'выбран' if is_checked else 'не выбран'}")

        # Кликаем только если нужно изменить состояние
        if not is_checked:
            self.get_radiobutton_5percent().click()
            print("Радио баттон 5% отмечен")
        else:
            print("Радио баттон 5% уже отмечен")

    def click_checkbox_city_filter(self):

        # Проверяем текущее состояние
        is_checked = self.get_checkbox_city_filter().is_selected()
        print(f"Текущее состояние чекбокса Тюмень ТЦ Фаворит: {'выбран' if is_checked else 'не выбран'}")

        # Кликаем только если нужно изменить состояние
        if not is_checked:
            self.get_checkbox_city_filter().click()
            print("Чекбокс Тюмень ТЦ Фаворит отмечен")
        else:
            print("Чекбокс Тюмень ТЦ Фаворит уже отмечен")

    def click_checkbox_zab5min(self):

        # Проверяем текущее состояние
        is_checked = self.get_checkbox_zab5min().is_selected()
        print(f"Текущее состояние чекбокса Забрать за 5 минут: {'выбран' if is_checked else 'не выбран'}")

        # Кликаем только если нужно изменить состояние
        if not is_checked:
            self.get_checkbox_zab5min().click()
            print("Чекбокс Забрать за 5 минут отмечен")
        else:
            print("Чекбокс Забрать за 5 минут уже отмечен")

    # Method

    def select_product_name_price(self):
        with allure.step("get product name, price"):
            Logger.add_start_step(method="get product name, price")
            self.get_product_name()
            self.get_value_price()
            Logger.add_end_step(url=self.driver.current_url, method="get product name, price")

    def go_product_card(self):
        with allure.step("go product card"):
            Logger.add_start_step(method="go product card")
            self.click_product_link()
            Logger.add_end_step(url=self.driver.current_url, method="go product card")

    def set_value_search(self):
        with allure.step("set value search"):
            Logger.add_start_step(method="set value search")
            self.driver.get(self.url)
            self.get_current_url()
            self.set_value_search_field()
            self.assert_url(self.url_after_search)
            Logger.add_end_step(url=self.driver.current_url, method="set value search")

    def select_city(self):
        with allure.step("select city"):
            Logger.add_start_step(method="select city")
            self.driver.get(self.url)
            self.get_current_url()
            self.set_city_selector()
            self.send_city_selector()
            self.click_city_fined()
            Logger.add_end_step(url=self.driver.current_url, method="select city")

    def select_popular_button(self):
        with allure.step("select popular button"):
            Logger.add_start_step(method="select popular button")
            self.click_popular_button()
            self.assert_word(self.get_main_word(), 'Стиральные машины с сушкой')
            print(self.get_main_word().text)
            Logger.add_end_step(url=self.driver.current_url, method="select popular button")

    def select_clean_button(self):
        with allure.step("select clean button"):
            Logger.add_start_step(method="select clean button")
            self.click_clean_button()
            Logger.add_end_step(url=self.driver.current_url, method="select clean button")

    def input_price_filter(self):
        with allure.step("input price filter"):
            Logger.add_start_step(method="input price filter1")
            self.send_price_filter_min()
            self.send_price_filter_max()
            Logger.add_end_step(url=self.driver.current_url, method="input price filter2")

    def select_shop_filter_link(self):
        with allure.step("select shop filter link"):
            Logger.add_start_step(method="select shop filter link")
            self.click_shop_filter_link()
            Logger.add_end_step(url=self.driver.current_url, method="select shop filter link")

    def set_checkbox_city_filter(self):
        with allure.step("set checkbox city filter"):
            Logger.add_start_step(method="set checkbox city filter")
            self.click_checkbox_city_filter()
            Logger.add_end_step(url=self.driver.current_url, method="set checkbox city filter")

    def set_checkbox_zab5min(self):
        with allure.step("checkbox zab5min"):
            Logger.add_start_step(method="checkbox zab5min")
            self.click_checkbox_zab5min()
            Logger.add_end_step(url=self.driver.current_url, method="checkbox zab5min")

    def click_radiobutton_5percent(self):
        with allure.step("set radio button 5%"):
            Logger.add_start_step(method="radiobutton 5percent")
            self.select_radiobutton_5percent()
            Logger.add_end_step(url=self.driver.current_url, method="radiobutton 5percent")

    def select_button_apply_filter(self):
        with allure.step("select button apply filter"):
            Logger.add_start_step(method="select button apply filter")
            self.click_get_button_apply_filter()
            Logger.add_end_step(url=self.driver.current_url, method="select button apply filter")

