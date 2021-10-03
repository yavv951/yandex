import time

import pytest
from common.constants import LoginConstants



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
        #app.image.find_images_on_page()
        app.image.current_ur()
        assert app.image.link_2() == "https://yandex.ru/", "Not table hints"
        time.sleep(3)



