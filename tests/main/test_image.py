import logging

logger = logging.getLogger(__name__)


class TestYandexImage:
    def test_yandex_image(self, app):
        """
        Steps
        1. Open yandex page
        2. Click on "Картинки"
        3. URL verification https://yandex.ru/images/
        3. Click on first image
        4. Compare the picture in the field with the name of the picture
        5. Click next image
        6. Click the previous photo
        7. Compare image
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
        assert text == text_image, "The name of the picture does not match"
        app.image.click_on_image()
        img = app.image.name_image()
        app.image.click_next_image()
        app.image.click_prev_image()
        img_2 = app.image.name_image()
        logger.info(f"image {img} = {img_2}")
        assert img == img_2, "This is not the photo"
