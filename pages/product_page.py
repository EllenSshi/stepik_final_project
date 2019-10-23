from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.should_be_the_same_product_name_in_message()
        #  print(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text)
        self.should_be_basket_price_like_product_price()
        #  time.sleep(5)

    def should_be_the_same_product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
                self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text, "product name in messages is not correct"

    def should_be_basket_price_like_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text, "product price in messages is not correct"
