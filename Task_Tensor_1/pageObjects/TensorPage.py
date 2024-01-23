from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure

# presence block element locator
check_block = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')

# name block element locator
name_block = (By.XPATH, "//p[contains(text(),'Сила в людях')]")

# more details block element locator
more_details = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')

# more details button element locator
more_details_button = (By.XPATH, "//div[@class='tensor_ru-Index__block4-bg']/descendant::a")


class TensorPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def switch_to_window_tensor(self):
        with allure.step("Switch to https://tensor.ru/"):
            return self.switch(self.browser.window_handles[1])

    def block_check(self):
        with allure.step("The block is displayed"):
            return self.find(check_block).is_displayed()

    def check_name_block(self):
        with allure.step("Checking block name"):
            return self.find(name_block).text

    def more_details_button_click(self):
        with allure.step("Scroll and go to more details button"):
            action = ActionChains(self.browser)
            action.move_to_element(self.find(more_details))
            action.click(self.find(more_details_button))
            action.perform()

