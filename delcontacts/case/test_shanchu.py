from page.mainpage import MainPage


class TestCase():
    def setup(self):
        self.mainpage = MainPage()


    def test_shanchu(self):

        result = self.mainpage.click_txl().person_data().editcy().search()
        assert  result == False








