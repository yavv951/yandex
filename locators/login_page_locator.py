from selenium.webdriver.common.by import By


class BasePageLocators:
    # поле поиска
    INPUT = (By.CLASS_NAME, "input__control")
    # таблица с подсказками
    TABLE_HINTS = (By.CLASS_NAME, "visibility_of_element_located")
    TENSOR_WEBSITE = (By.CLASS_NAME, "organic__url-text")
    BUTTON_INPUT = (By.CLASS_NAME, "button_theme_search")
    SEARCH_RESULTS = (By.CLASS_NAME, "mini-suggest__item_type_fulltext")
    IMAGE_BUTTON = (By.XPATH, "//*[text()='Картинки']")
    DEVELOPMENT_SOFTWARE = (By.XPATH, "//*[text()='О компании']")
    # картинки
    IMAGE = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")

    IMAGE_TEXT = (By.CLASS_NAME, 'PopularRequestList-SearchText')
    TEXT = (By.NAME, "Text")
    INPUT_TEXT = (By.CLASS_NAME, 'input__control')

    GALLERY_IMAGE = (By.CLASS_NAME, "MMGallery-ItemImageOverlay")
    FIRST_IMAGE = (By.CLASS_NAME, "serp-item__link")
    PREV_IMAGE = (By.CLASS_NAME, "CircleButton_type_prev")
    NEXT_IMAGE = (By.CLASS_NAME, "CircleButton_type_next")