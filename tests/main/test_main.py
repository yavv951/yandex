from common.constants import LoginConstants


class TestYandex:
    def test_yandex_input(self, app):
        """
        Steps
        1. Open yandex page
        2. Enter the Tensor in the search
        3. Check that a table with hints has appeared
        4. Click on tensor website
        5. Click on "О компании"
        """
        app.open_main_page()
        app.yandex.search_fields()
        assert app.yandex.open_table_hints(), "Not table hints"
        app.yandex.click_on_button()
        app.yandex.click_go_to_website()
        app.yandex.find_about_company_button()
        assert LoginConstants.ABOUT_COMPANY == app.yandex.find_about_company(), "We are not tensor website"
