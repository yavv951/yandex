import logging
import time

import pytest
from common.constants import LoginConstants
logger = logging.getLogger(__name__)


@pytest.mark.auth
class TestYandexImage:
    def test_yandex_image(self, app):
        """
        Steps
        1. Open yandex page
        2. Enter the Tensor in the search
        3. Check that a table with hints has appeared
        4. Click on tensor website
        5. Click on "О компании"
        """
        app.open_main_page()
        app.image.click_image_button()
        app.switch_to_window()
        url = app.image.current_url()
        assert "https://yandex.ru/images/" in url, "The urls don't match"
        logger.info(f"image_url {url} ")
        text = app.image.get_first_image_text()
        app.image.click_first_image()
        app.refresh()
        text_image = app.image.get_image_text_on_input()
        logger.info(f"image_text {text} = {text_image}")
        assert text == text_image, "The name of the picture does not match "
        app.image.click_on_image()
        app.image.click_next_image()
        app.image.click_prev_image()
        time.sleep(3)







