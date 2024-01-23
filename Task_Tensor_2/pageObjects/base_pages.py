# class is the parent of all pages
class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def finds(self, args):
        return self.browser.find_elements(*args)

    def switch(self, args):
        return self.browser.switch_to.window(args)

    def execute(self, args):
        return self.browser.execute_script(args)