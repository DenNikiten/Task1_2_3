from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.BasePage import BasePage
import allure


class SbisPage(BasePage):
    # flag element locator
    flag_demo = (By.LINK_TEXT, "Демо")

    # download button sbis element locator
    btn_link_download_sbis = (By.LINK_TEXT, "Скачать СБИС")

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step("Open https://sbis.ru/"):
            self.browser.get('https://sbis.ru/')

    def download_sbis_is_displayed(self):
        with allure.step("Download sbis button is displayed"):
            return self.find(self.btn_link_download_sbis).is_displayed()

    def download_sbis_button_click(self):
        with allure.step("Scroll and go to download sbis button"):
            action = ActionChains(self.browser)
            action.move_to_element(self.find(self.flag_demo))
            action.perform()
            self.find(self.btn_link_download_sbis).click()

