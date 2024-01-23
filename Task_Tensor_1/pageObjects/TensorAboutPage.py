from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

# working field element locator
section_working = (By.CLASS_NAME, "tensor_ru-About__block3")

# height width element locator
width_height_xpath = (By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper']/child::img")


class TensorAboutPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def section_working_is_displayed(self):
        with allure.step("The section is displayed - Working"):
            return self.find(section_working).is_displayed()

    @property
    def same_height_and_width(self):
        with allure.step("Timeline photographs have the same height and width"):
            list_width = []
            list_height = []
            [list_width.append(int(item.get_attribute('width'))) for item in self.finds(width_height_xpath)]
            [list_height.append(int(item.get_attribute('height'))) for item in self.finds(width_height_xpath)]
            return len(set(list_height)), len(set(list_width))
