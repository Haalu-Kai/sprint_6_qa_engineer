import allure
from pages.base_page import BasePage
from utils.locators import BasePageLocator
from utils.locators import YaScooterHomePageLocator as Locators


class YaScooterHomePage(BasePage):

    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        self.find_element(Locators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        self.find_element(Locators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        elems[question_number].click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_to_window(self, window_number: int = 1):
        self.switch_to_window(window_number)

    @allure.step('Ожидать, пока URL не станет не about:blank')
    def wait_url_until_not_about_blank(self, time: int = 10):
        self.wait_url_until_not_about_blank(time)

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        self.find_element(BasePageLocator.YANDEX_SITE_BUTTON).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        self.find_element(BasePageLocator.COOKIE_ACCEPT_BUTTON).click()
