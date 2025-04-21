
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

import allure


class Product_card_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.product_price_pc = None
        self.value_price = None
        self.product_name_pc = None
        # self.Main_page = None
        self.driver = driver

    # Locators

    product_name_full = ("//div[@data-meta-name='ProductHeaderLayout__title']//h1[contains(@class, "
                         "'StyledProductTitle')]")

    price_product_card = "[data-meta-name='PriceBlock__price']"

    button_basket = "//button[@data-meta-name='BasketDesktopButton']"

    # Getter

    def get_product_full_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.product_name_full)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.price_product_card)))

    def get_button_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_basket)))

    # Action
    def click_button_basket(self):
        self.get_button_basket().click()
        print("Click basket button")


    def get_product_full_name_value(self):
        value_product_full_name = self.get_product_full_name().text
        # value_small_product_name = value_product_full_name.split(',', 1)[0]
        print(f"Full product name: {value_product_full_name}")

    def get_product_name_pc(self):
        self.product_name_pc = None
        self.product_name_pc = self.get_product_full_name().get_attribute('textContent').strip() or "Элемент не найден"
        print(f"Product name: {self.product_name_pc}")
        return self.product_name_pc

    # Method
    def get_product_price_pc(self):
        with allure.step("get product price pc"):
            Logger.add_start_step(method="get product price pc")
            self.product_price_pc = self.get_price().text[:-1].replace(" ", "")
            print(f"Product PRICE pc: {self.product_price_pc}")
            Logger.add_end_step(url=self.driver.current_url, method="get product price pc")
            return self.product_price_pc

    def select_full_name_product(self):
        with allure.step("select full name product"):
            Logger.add_start_step(method="select full name product")
            self.get_product_full_name_value()
            Logger.add_end_step(url=self.driver.current_url, method="select full name product")

    def add_product_basket(self):
        with allure.step("add product to basket"):
            Logger.add_start_step(method="add product to basket")
            self.click_button_basket()
            Logger.add_end_step(url=self.driver.current_url, method="add product to basket")
