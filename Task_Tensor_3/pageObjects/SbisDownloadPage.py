import os
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage
import allure
from selenium import webdriver


class SbisDownloadPage(BasePage):
    # sbis plugin tabbutton element locator
    folder_plugin_xpath = (By.XPATH, "//div[@class='sbis_ru-VerticalTabs__left']/descendant::div[10]")

    # link for download plugin element locator
    plugin_xpath = (By.XPATH, '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

    def __init__(self, browser):
        super().__init__(browser)

    def click_plugin_tab(self):
        with allure.step("Sbis plugin tabbutton click"):
            return self.find(self.folder_plugin_xpath).click()

    def options(self):
        with allure.step("Method for bypassing blocking and downloading a file to a folder"):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("prefs", {
                "download.default_directory": "C:\Task_Tensor_3",
                "download.prompt_for_download": False
            })
            chrome_options.add_argument("--headless")
            self.browser.command_executor._commands["send_command"] = (
                "POST", '/session/$sessionId/chromium/send_command')
            params = {
                'cmd': 'Page.setDownloadBehavior',
                'params': {
                    'behavior': 'allow',
                    'downloadPath': "C:\Task_Tensor_3"
                }
            }
            command_result = self.browser.execute("send_command", params)
            return command_result

    def click_plugin_for_download(self):
        with allure.step("Click sbis plugin for download web-installer"):
            self.find(self.plugin_xpath).click()

    @staticmethod
    def download_file_in_folder():
        with allure.step("Checking that the file has been downloaded"):
            dir_path = "C:\Task_Tensor_3"
            result = os.listdir(dir_path)
            return result

    @staticmethod
    def file_size():
        dir_path_file = "C:\Task_Tensor_3\sbisplugin-setup-web.exe"
        size_file = str(round(os.path.getsize(dir_path_file) / (1024 * 1024), 2)) + ' МБ'
        return size_file
