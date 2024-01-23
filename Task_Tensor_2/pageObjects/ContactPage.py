from selenium.webdriver.common.by import By
from pageObjects.base_pages import BasePage
import allure


class ContactPage(BasePage):
    # contacts button element locator
    button_contacts_xpath = (By.XPATH, "//li[contains(@class, 'sbisru-Header__menu-item-1')]/child::a")

    # region element locator
    region_xpath = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']/child::span")

    # presence list partners element locator
    presence_list_partners_xpath = (By.CLASS_NAME, "sbisru-Contacts-List__col")

    # change button region element locator
    btn_change_region = (By.XPATH, "//span[@title='Камчатский край']")

    # list partners element locator
    partners_list_xpath = (By.XPATH, "//div[@class='sbisru-Contacts-List__col-1']/child::div[1]")

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://sbis.ru/')

    def click_contacts_btn(self):
        with allure.step('Open contacts page'):
            self.find(self.button_contacts_xpath).click()

    def check_region_xpath(self):
        return self.find(self.region_xpath).text

    def check_list_partners_is_displayed(self):
        with allure.step("List partners is displayed"):
            return self.find(self.presence_list_partners_xpath).is_displayed()

    def go_to_window_change_region(self):
        with allure.step('Click the button to change the region, open the window'):
            self.find(self.region_xpath).click()

    def change_region(self):
        with allure.step('Region change button, click'):
            self.find(self.btn_change_region).click()

    def extract_title(self):
        return self.execute("return document.title;")

    def list_ekb(self):
        with allure.step('Save ekb contacts'):
            list_company_names_ekb = []
            [list_company_names_ekb.append(item.get_attribute('title')) for item in self.finds(self.partners_list_xpath)]
            return list_company_names_ekb

    def list_kamchatka(self):
        with allure.step('Save kamchatka contacts'):
            list_company_names_kamchatka = []
            [list_company_names_kamchatka.append(item.get_attribute('title')) for item in self.finds(self.partners_list_xpath)]
            list_company_names_kamchatka = list_company_names_kamchatka[0]
            return list_company_names_kamchatka
