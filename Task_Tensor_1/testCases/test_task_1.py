from pageObjects.TensorPage import TensorPage
from pageObjects.ContactPage import ContactPage
from pageObjects.TensorAboutPage import TensorAboutPage
from utilitiesPackage.logger import LogGen


class TestTask1:
    # generateLog Object
    generateLog = LogGen.genlog()

    def test_case_1_contacts(self, browser):
        # log
        self.generateLog.info("***test1. Open contacts page***")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test1. Open https://sbis.ru/")
        contacts_page.open()
        # log
        self.generateLog.info("test1. Click button. Go to contacts page")
        contacts_page.button()

    def test_case_2_find_banner_tensor_and_click(self, browser):
        # log
        self.generateLog.info("***test2. Find banner tensor and click***")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test2. Open https://sbis.ru/")
        contacts_page.open()
        # log
        self.generateLog.info("test2. Click button. Go to contacts page")
        contacts_page.button()

        # log
        self.generateLog.info("test2. Banner tensor is displayed")
        if contacts_page.banner_tensor():
            # log
            self.generateLog.info("test2. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test2. Failed")
            assert False

        # log
        self.generateLog.info("test2. Click on the banner tensor")
        contacts_page.button2_click()

    def test_case_3_switch_to_tensor_website(self, browser):
        # log
        self.generateLog.info("***test3. Switch to tensor website***")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test3. Open https://sbis.ru/")
        contacts_page.open()
        # log
        self.generateLog.info("test3. Click button. Go to contacts page")
        contacts_page.button()
        # log
        self.generateLog.info("test3. Click on the banner tensor")
        contacts_page.button2_click()
        # log
        self.generateLog.info("test3. tensor_page Object")
        tensor_page = TensorPage(browser)
        # log
        self.generateLog.info("test3. Switch to https://tensor.ru/")
        tensor_page.switch_to_window_tensor()

        # log
        self.generateLog.info("test3. Checking that https://tensor.ru/ opens")
        if browser.current_url == "https://tensor.ru/":
            # log
            self.generateLog.info("test3. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test3. Failed")
            assert False

    def test_case_4_check_block(self, browser):
        # log
        self.generateLog.info("***test4. Check block***")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test4. Open https://sbis.ru/")
        contacts_page.open()
        # log
        self.generateLog.info("test4. Click button. Go to contacts page")
        contacts_page.button()
        # log
        self.generateLog.info("test4. Click on the banner tensor")
        contacts_page.button2_click()
        # log
        self.generateLog.info("test4. tensor_page Object")
        tensor_page = TensorPage(browser)
        # log
        self.generateLog.info("test4. Switch to https://tensor.ru/")
        tensor_page.switch_to_window_tensor()

        # log
        self.generateLog.info("test4. The block is displayed")
        if tensor_page.block_check():
            # log
            self.generateLog.info("test4. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test4. Failed")
            assert False

        # log
        self.generateLog.info("test4. Checking block name")
        if tensor_page.check_name_block() == 'Сила в людях':
            # log
            self.generateLog.info("test4. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test4. Failed")
            assert False

    def test_5_go_to_more_details_button(self, browser):
        # log
        self.generateLog.info("***test5. Go to more details button***")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test5. Open https://sbis.ru/")
        contacts_page.open()
        # log
        self.generateLog.info("test5. Click button. Go to contacts page")
        contacts_page.button()
        # log
        self.generateLog.info("test5. Click on the banner tensor")
        contacts_page.button2_click()
        # log
        self.generateLog.info("test5. tensor_page Object")
        tensor_page = TensorPage(browser)
        # log
        self.generateLog.info("test5. Switch to https://tensor.ru/")
        tensor_page.switch_to_window_tensor()
        # log
        self.generateLog.info("test5. Scroll and go to more details button")
        tensor_page.more_details_button_click()

        # log
        self.generateLog.info("test5. Checking that https://tensor.ru/about opens")
        if browser.current_url == "https://tensor.ru/about":
            # log
            self.generateLog.info("test5. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test5. Failed")
            assert False

    def test_6_section_working_and_the_same_height_width_photographs(self, browser):
        # log
        self.generateLog.info("test6. The section is displayed - Working and have the same height and width photographs")
        contacts_page = ContactPage(browser)
        # log
        self.generateLog.info("test6. Open https://sbis.ru/")
        contacts_page.open()
        # log
        self.generateLog.info("test6. Click button. Go to contacts page")
        contacts_page.button()
        # log
        self.generateLog.info("test6. Click on the banner tensor")
        contacts_page.button2_click()
        # log
        self.generateLog.info("test6. tensor_page Object")
        tensor_page = TensorPage(browser)
        # log
        self.generateLog.info("test6. Switch to https://tensor.ru/")
        tensor_page.switch_to_window_tensor()
        # log
        self.generateLog.info("test6. Scroll and go to more details button")
        tensor_page.more_details_button_click()
        # log
        self.generateLog.info("test6. tensor_about_page Object")
        tensor_about_page = TensorAboutPage(browser)

        # log
        self.generateLog.info("test6. The section is displayed - Working")
        if tensor_about_page.section_working_is_displayed():
            # log
            self.generateLog.info("test6. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test6. Failed")
            assert False

        # log
        self.generateLog.info("test6. Timeline photographs have the same height and width")
        if tensor_about_page.same_height_and_width == (1, 1):
            # log
            self.generateLog.info("test6. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test6. Failed")
            assert False
