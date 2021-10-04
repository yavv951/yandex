import logging

from pages.image_page import YandexImagePage
from pages.main_page import YandexPage

logger = logging.getLogger("moodle")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.yandex = YandexPage(self)
        self.image = YandexImagePage(self)

    def quit(self):
        self.driver.quit()


    def open_main_page(self):
        logger.info("open " + self.url)
        self.driver.get(self.url)

    def switch_to_window(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def refresh(self):
        self.driver.refresh()