from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.should_be_the_same_product_name_in_message()
        self.should_be_basket_price_like_product_price()
        time.sleep(3)

    def should_be_the_same_product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in \
                self.browser.find_element(*ProductPageLocators.MESSAGES).text, "product name in messages is not correct"

    def should_be_basket_price_like_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.split("&nbsp;")[0] in \
               self.browser.find_element(*ProductPageLocators.MESSAGES).text, "product price in messages is not correct"
