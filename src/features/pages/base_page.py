
class BasePage:
    BASE_URL = "https://tap-ht25-testverktyg.github.io/exam/"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL)

    def click_button(self, name):
        self.page.get_by_role("button", name=name).click()
