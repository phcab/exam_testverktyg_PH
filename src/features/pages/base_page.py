
class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
