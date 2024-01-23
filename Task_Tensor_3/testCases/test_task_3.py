import time
from pageObjects.SbisDownloadPage import SbisDownloadPage
from utilitiesPackage.logger import LogGen
from pageObjects.SbisPage import SbisPage


class TestTask1:
    # generateLog Object
    generateLog = LogGen.genlog()

    def test_case_1_go_to_sbis(self, browser):
        # log
        self.generateLog.info("***test1. Open sbis page***")
        sbis_page = SbisPage(browser)
        # log
        self.generateLog.info("test1. Open https://sbis.ru/")
        sbis_page.open()

    def test_case_2_go_to_download_sbis(self, browser):
        # log
        self.generateLog.info("***test2. Go to download sbis page***")
        sbis_page = SbisPage(browser)
        # log
        self.generateLog.info("test2. Open https://sbis.ru/")
        sbis_page.open()

        # log
        self.generateLog.info("test2. Checking that download sbis is displayed")
        if sbis_page.download_sbis_is_displayed():
            # log
            self.generateLog.info("test2. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test2. Failed")
            assert False

        # log
        self.generateLog.info("test2. Click on the download sbis btn")
        sbis_page.download_sbis_button_click()

    def test_case_3_download_sbis_plugin(self, browser):
        # log
        self.generateLog.info("***test3. Download sbis plugin***")
        sbis_page = SbisPage(browser)
        # log
        self.generateLog.info("test3. Open https://sbis.ru/")
        sbis_page.open()
        # log
        self.generateLog.info("test3. Click on the download sbis btn")
        sbis_page.download_sbis_button_click()

        # log
        self.generateLog.info("test3. Time to switch to plugin")
        time.sleep(1)

        sbis_download_page = SbisDownloadPage(browser)
        # log
        self.generateLog.info("test3. Go to sbis plugin tabbutton")
        sbis_download_page.click_plugin_tab()
        # log
        self.generateLog.info("test3. Options for downloading a file to a folder")
        sbis_download_page.options()
        # log
        self.generateLog.info("test3. Click sbis plugin for download web-installer")
        sbis_download_page.click_plugin_for_download()
        # log
        self.generateLog.info("test3. Time to download the file to the folder")
        time.sleep(10)

    def test_case_4_download_file(self, browser):
        # log
        self.generateLog.info("***test4. Download file web-installer***")
        sbis_page = SbisPage(browser)
        # log
        self.generateLog.info("test4. Open https://sbis.ru/")
        sbis_page.open()
        # log
        self.generateLog.info("test4. Click on the download sbis btn")
        sbis_page.download_sbis_button_click()

        # log
        self.generateLog.info("test4. Time to switch to plugin")
        time.sleep(1)

        sbis_download_page = SbisDownloadPage(browser)
        # log
        self.generateLog.info("test4. Go to sbis plugin tabbutton")
        sbis_download_page.click_plugin_tab()
        # log
        self.generateLog.info("test4. Options for downloading a file to a folder")
        sbis_download_page.options()
        # log
        self.generateLog.info("test4. Click sbis plugin for download web-installer")
        sbis_download_page.click_plugin_for_download()
        # log
        self.generateLog.info("test4. Time to download the file to the folder")
        time.sleep(10)

        # log
        self.generateLog.info("test4. Checking that the file has been downloaded")
        if 'sbisplugin-setup-web.exe' in sbis_download_page.download_file_in_folder():
            # log
            self.generateLog.info("test4. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test4. Failed")
            assert False

    def test_case_5_check_file_size(self, browser):
        # log
        self.generateLog.info("***test5. Check file size***")
        sbis_page = SbisPage(browser)
        # log
        self.generateLog.info("test5. Open https://sbis.ru/")
        sbis_page.open()
        # log
        self.generateLog.info("test5. Click on the download sbis btn")
        sbis_page.download_sbis_button_click()

        # log
        self.generateLog.info("test5. Time to switch to plugin")
        time.sleep(1)

        sbis_download_page = SbisDownloadPage(browser)
        # log
        self.generateLog.info("test5. Go to sbis plugin tabbutton")
        sbis_download_page.click_plugin_tab()
        # log
        self.generateLog.info("test5. Options for downloading a file to a folder")
        sbis_download_page.options()
        # log
        self.generateLog.info("test5. Click sbis plugin for download web-installer")
        sbis_download_page.click_plugin_for_download()
        # log
        self.generateLog.info("test5. Time to download the file to the folder")
        time.sleep(10)

        # log
        self.generateLog.info("test5. Checking the size of the downloaded file in MB")
        if '7.02 МБ' == sbis_download_page.file_size():
            # log
            self.generateLog.info("test5. Passed")
            assert True
        else:
            # log
            self.generateLog.info("test5. Failed")
            assert False

