from selenium.webdriver.remote.webelement import WebElement
import logging
from locators.login_page_locator import BasePageLocators
from models.auth import AuthData
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


class YandexImagePage(BasePage):
    def click_image_button(self):
        element = self.find_element(BasePageLocators.IMAGE_BUTTON)
        self.click_element(element)


    def find_images_on_page(self):
        self.click_element(self.find_element(BasePageLocators.IMAGE_TEXT)[0])


    def link_2(self):
        return self.link()

