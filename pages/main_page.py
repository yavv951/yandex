from selenium.webdriver.remote.webelement import WebElement
import logging
from locators.login_page_locator import BasePageLocators
from models.auth import AuthData
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


class YandexPage(BasePage):

    def search_fields(self):
        element = self.find_element(BasePageLocators.INPUT)
        self.fill_element(element, "Тензор")

    def click_on_button(self):
        element = self.find_element(BasePageLocators.BUTTON_INPUT)
        self.click_element(element)

    def open_table_hints(self):
        element = self.find_all_elements(BasePageLocators.SEARCH_RESULTS)
        if len(element) > 4:
            return True
        else:
            return False

    def click_go_to_website(self):
        element = self.find_element(BasePageLocators.TENSOR_WEBSITE)
        self.click_element(element)

    def find_about_company_button(self):
        element = self.find_element(BasePageLocators.DEVELOPMENT_SOFTWARE)
        self.click_element(element)

    def find_about_company(self):
        return self.find_element(BasePageLocators.DEVELOPMENT_SOFTWARE).text

    def click_image_button(self):
        element = self.find_element(BasePageLocators.IMAGE_BUTTON)
        self.click_element(element)


