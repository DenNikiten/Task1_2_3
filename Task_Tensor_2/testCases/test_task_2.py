import time
import allure
from pageObjects.ContactPage import ContactPage
from utilitiesPackage.logger import LogGen


class TestTask2:
    # generateLog Object
    generateLog = LogGen.genlog()

    def test_case_1_contacts(self, browser):
        # log
        self.generateLog.info("test1. Open contacts page")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test1. Open https://sbis.ru/")
        contacts_page.open()
        # log
        self.generateLog.info("test1. Click button. Go to contacts page")
        contacts_page.click_contacts_btn()

    def test_case_2_region_partners(self, browser):
        # log
        self.generateLog.info("test2. Checking the region and list of partners")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test2. Open contacts page")
        contacts_page.open()
        contacts_page.click_contacts_btn()

        # log
        self.generateLog.info("test2. Expected region is Свердловская область")
        if contacts_page.check_region_xpath() == 'Свердловская обл.':
            # log
            self.generateLog.info("test2. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test2. Failed")
            assert False

        # log
        self.generateLog.info("test2. List partners is displayed")
        if contacts_page.check_list_partners_is_displayed():
            assert True
            # log
            self.generateLog.info("test2. Passed")
        else:
            # log
            self.generateLog.info("test2. Failed")
            assert False

    def test_case_3_change_region(self, browser):
        # log
        self.generateLog.info("test3. Change region")

        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test3. Open contacts page")
        contacts_page.open()
        contacts_page.click_contacts_btn()

        # log
        self.generateLog.info("test3. Go to the window to change the region")
        contacts_page.go_to_window_change_region()

        # log
        self.generateLog.info("test3. Go to the window to change the region")

        # log
        self.generateLog.info("test3. Click on a region to change it")
        contacts_page.change_region()

    @allure.feature('test4. Data_checking')
    @allure.story('url, title, list_partners, new_region')
    def test_case_4_data_checking(self, browser):
        # log
        self.generateLog.info("test4. Data checking: region, title, url, list of partners")
        contacts_page = ContactPage(browser)

        # log
        self.generateLog.info("test4. Open contacts page")
        contacts_page.open()
        contacts_page.click_contacts_btn()

        # log
        self.generateLog.info("test4. Save ekb contacts")
        ekb_list = contacts_page.list_ekb()

        # log
        self.generateLog.info("test4. Go to the window to change the region")
        contacts_page.go_to_window_change_region()

        # log
        self.generateLog.info("test4. Click on a region to change it")
        contacts_page.change_region()

        # log
        self.generateLog.info("test4. Data checking: region, title, url, list of partners")

        with allure.step('Time to substitute the selected region'):
            time.sleep(1)

        # log
        self.generateLog.info("test4. Save ekb contacts")
        kamchatka_list = contacts_page.list_kamchatka()

        # log
        self.generateLog.info("test4. Data checking")
        # log
        self.generateLog.info("test4. Checking for new region substitution")
        with allure.step('Checking for new region substitution'):
            if contacts_page.check_region_xpath() == 'Камчатский край':
                # log
                self.generateLog.info("test4. Passed")
                assert True
            else:
                # log
                self.generateLog.info("test4. Failed")
                assert False

        # log
        self.generateLog.info("test4. Selected region in url")
        with allure.step('Selected region in url'):
            if '41-kamchatskij-kraj' in browser.current_url:
                # log
                self.generateLog.info("test4. Passed")
                assert True
            else:
                # log
                self.generateLog.info("test4. Failed")
                assert False

        # log
        self.generateLog.info("test4. Selected region in title")
        with allure.step('Selected region in title'):
            if 'Камчатский край' in contacts_page.extract_title():
                # log
                self.generateLog.info("test4. Passed")
                assert True
            else:
                # log
                self.generateLog.info("test4. Failed")
                assert False

        # log
        self.generateLog.info("test4. The list of partners has changed")
        with allure.step('The list of partners has changed'):
            if kamchatka_list not in ekb_list:
                # log
                self.generateLog.info("test4. Passed")
                assert True
            else:
                # log
                self.generateLog.info("test4. Failed")
                assert False

