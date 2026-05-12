import allure
from utils.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключиться на вкладку браузера')
    def switch_to_window(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Ожидать, пока URL не станет не about:blank')
    def wait_url_until_not_about_blank(self, time: int = 10):
        WebDriverWait(self.driver, time).until_not(
            EC.url_to_be('about:blank')
        )
