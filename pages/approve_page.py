from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import Main_page
from base.base_class import Base
from utilities.logger import Logger

import allure


class Approve_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.value_product_price = None
        self.value_name_product = None
        self.driver = driver

    # Locators
    product_added_world = "//div[@class='app-catalog-7wfj11-StyledTitle eqmkmq80']"
    button_go_basket = "(//button[contains(@class, 'StyledButton')]//span[contains(text(), 'Перейти в корзину')])[1]"
    name_product = "//div[@class='app-catalog-1vbitm3-StyledTitle e1hg4b130']"
    product_price = ".app-catalog-1qcsymx-MetaWrapper--StyledMetaWrapper[data-meta-is-total=\'notTotal\']"

    # Gets
    def get_product_added_world(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_added_world)))

    def get_button_go_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_basket)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.name_product)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(( By.CSS_SELECTOR, self.product_price)))

    # Action
    def find_product_added_world(self):
        self.get_product_added_world()
        print("The product has been added to the cart")

    def find_product_price(self):
        self.value_product_price = self.get_product_price().text[:-1].replace(" ", "")
        print(f"Product price approve page {self.value_product_price}")
        return self.value_product_price

    def click_button_go_basket(self):
        self.get_button_go_basket().click()
        print("Click button go basket")

    def set_name_product(self):
        self.value_name_product = self.get_name_product().text
        print(f"Set name product from approve page {self.value_name_product}")
        return self.value_name_product

    # Method
    def select_product_price(self):
        with allure.step("select product price"):
            Logger.add_start_step(method="select product price")
            self.find_product_price()
            Logger.add_end_step(url=self.driver.current_url, method="select product price")

    def select_button_go_basket(self):
        with allure.step("select button go basket"):
            Logger.add_start_step(method="select button go basket")
            self.click_button_go_basket()
            Logger.add_end_step(url=self.driver.current_url, method="select button go basket")

    def select_name_product(self):
        with allure.step("select name product"):
            Logger.add_start_step(method="select name product")
            self.set_name_product()
            Logger.add_end_step(url=self.driver.current_url, method="select name product")

    def select_product_added_world(self):
        with allure.step("The product has been added to the cart"):
            Logger.add_start_step(method="The product has been added to the cart")
            self.find_product_added_world()
            Logger.add_end_step(url=self.driver.current_url, method="The product has been added to the cart")