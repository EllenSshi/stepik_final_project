from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(@href,'/basket/')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD_FIELD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]//p/strong")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")
