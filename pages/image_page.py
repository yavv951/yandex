#from selenium.webdriver.remote.webelement import WebElement
import logging
from locators.login_page_locator import BasePageLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class YandexImagePage(BasePage):
    def click_image_button(self):
        element = self.find_element(BasePageLocators.IMAGE_BUTTON)
        self.click_element(element)

    def find_images_on_page(self):
        self.click_element(self.find_element(BasePageLocators.IMAGE_TEXT)[0])

    def get_first_image_text(self):
        text = self.find_element(BasePageLocators.IMAGE).text
        return text

    def click_first_image(self):
        element = self.find_element(BasePageLocators.IMAGE)
        self.click_element(element)

    def get_image_text_on_input(self):
        element = self.find_element(BasePageLocators.INPUT)
        return element.get_attribute("value")

    def click_on_image(self):
        element = self.find_element(BasePageLocators.FIRST_IMAGE)
        self.click_element(element)

    def name_image(self):
        img = self.find_element(BasePageLocators.GALLERY_IMAGE)
        logger.info(f"image src {img}")
        return img.get_attribute("src")

    def click_next_image(self):
        element = self.find_element(BasePageLocators.NEXT_IMAGE)
        self.click_element(element)

    def click_prev_image(self):
        element = self.find_element(BasePageLocators.PREV_IMAGE)
        self.click_element(element)


