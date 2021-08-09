from data.data import Data
from pages.base import BasePage
from data.locators import LogInPageLocator
from time import sleep
import allure


class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = LogInPageLocator
        self.data = Data
        super().__init__(driver)

    def sign_in(self):
        self.click(self.locator.login_link)
        self.send_data(self.data.email, self.locator.email)
        sleep(1)
        self.click(self.locator.login)
        self.send_data(self.data.password, self.locator.password)
        self.click(self.locator.login1)
        print('successfully logged-In')

    @allure.step("verify sign in")
    def verify_sign_in(self):
        self.sign_in()

        # open
        self.click(self.locator.boards)
        sleep(1)
        self.click(self.locator.board)
        sleep(2)
        # create card
        # sleep(1)
        # self.click(self.locator.add_card_column1)
        # sleep(1)
        # self.send_data(self.data.card_title, self.locator.card_title1)
        # sleep(1)
        # self.click(self.locator.add_card1)
        # sleep(2)

        # see card detail
        # self.click(self.locator.card1)

        # delete card
        # self.right_click(*self.locator.card1)
        # sleep(2)
        # self.click(self.locator.delete_card)
        # sleep(3)

        # drag and drop card/ move card
        self.drag_and_drop(self.locator.source_card, self.locator.destination_cared_list)
        sleep(4)

        # create list
        # self.click(self.locator.create_list)
        # sleep(1)
        # self.send_data(self.data.list_title, self.locator.list_title)
        # sleep(1)
        # self.click(self.locator.add_list)
        # sleep(1)
