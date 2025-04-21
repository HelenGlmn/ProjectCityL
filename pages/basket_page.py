from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

import allure
import time


class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.value_word_finish = None
        self.value_product_price = None
        self.value_name_product = None
        self.driver = driver

    # Locators

    world = "//span[contains(text(), 'Корзина')]"
    button_go_finish = "//span[contains(text(), 'Перейти к оформлению')]"
    name_product = ".css-13g6m7h-Flex--StyledFlex > a"
    product_price = "(//span[@data-meta-is-total='notTotal'])[1]"
    word_finish = "//div[@data-meta-name='Popup']//div[@class='css-0 ei3i9gr0']//span[@color='None']"

    # value_finish = 'Зарегистрируйтесь или войдите в свой аккаунт, чтобы получить баллы за покупку'
    # word_finish = "/html/body/div[4]/div/div/div/div/div/div[2]/span"

    # Gets
    def get_word_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_finish)))

    def get_world(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.world)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.name_product)))

    def get_button_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_finish)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.product_price)))

    # Action
    def select_world(self):
        self.get_world()
        print("Select main word Корзина")

    def set_finish_word(self):
        self.value_word_finish = self.get_word_finish().text
        print(f"Get finish word {self.value_word_finish}")
        return self.value_word_finish

    def set_button_finish(self):
        self.get_button_finish().click()
        print("Set finish button")

    def set_product_price(self):
        self.value_product_price = self.get_product_price().text[:-1].replace(" ", "")
        print(f"Set product price on basket page {self.value_product_price}")
        return self.value_product_price

    #
    def set_name_product(self):
        self.value_name_product = (self.get_product_name().get_attribute("title"))
        print(f"Set name product checkout page {self.value_name_product}")
        return self.value_name_product

    # Method
    def select_finish_word(self):
        with allure.step("select finish_word"):
            Logger.add_start_step(method="select finish_word")
            self.set_finish_word()
            self.assert_word(self.get_word_finish(), 'Зарегистрируйтесь или войдите в свой аккаунт, чтобы получить '
                                                     'баллы за покупку')
            print("Finish: остановимся пока на ЭТОМ")
            Logger.add_end_step(url=self.driver.current_url, method="select finish_word")

    def click_button_finish(self):
        with allure.step("click finish button"):
            Logger.add_start_step(method="click finish button")
            self.set_button_finish()
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="click finish button")

    def select_product_price(self):
        with allure.step("select product price"):
            Logger.add_start_step(method="select product price")
            self.set_product_price()
            Logger.add_end_step(url=self.driver.current_url, method="select product price")

    def select_product_name(self):
        with allure.step("select product name"):
            Logger.add_start_step(method="select product name")
            self.set_name_product()
            Logger.add_end_step(url=self.driver.current_url, method="select product name")

    def select_word(self):
        with (allure.step("select word")):
            Logger.add_start_step(method="select word")
            self.set_name_product()
            Logger.add_end_step(url=self.driver.current_url, method="select word")
