from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

# contacts button element locator
button_selector = (By.XPATH, "//li[contains(@class, 'sbisru-Header__menu-item-1')]/child::a")

# banner tensor button element locator
button_selector2 = (By.XPATH, '//div[@id="contacts_clients"]/descendant::a[@href="https://tensor.ru/"]')


class ContactPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step("Open https://sbis.ru/"):
            self.browser.get('https://sbis.ru/')

    def button(self):
        with allure.step("Click button. Go to contacts page"):
            self.find(button_selector).click()

    def banner_tensor(self):
        with allure.step("Banner tensor is displayed"):
            return self.find(button_selector2).is_displayed()

    def button2_click(self):
        with allure.step("Click on the banner tensor"):
            self.find(button_selector2).click()
