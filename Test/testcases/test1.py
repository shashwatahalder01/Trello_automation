from pages.signin_page import SignInPage
from testcases.base_test import BaseTest


class TestSignIn(BaseTest):

    def test_sign_in(self):
        page_sign_in = SignInPage(self.driver)
        page_sign_in.verify_sign_in()

# python3 -m unittest testcases.test1
# python3 -m pytest -s testcases/test1.py --alluredir=ReportAllure &&  allure serve ReportAllure/
