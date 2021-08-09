from selenium.webdriver.common.by import By


class LogInPageLocator(object):
    login_link = (By.XPATH, '//a[normalize-space()="Log in"]')
    email = (By.XPATH, '//input[@id="user"]')
    password = (By.XPATH, '//input[@id="password"]')
    login = (By.XPATH, '//input[@id="login"]')
    login1 = (By.XPATH, '//button[@id="login-submit"]')
    # continue_with_google = (By.XPATH, '//span[contains(text(),"Continue with Google")]')
    # continue_with_google_next = (By.XPATH, '//span[contains(text(),"পরবর্তী")]')

    boards = (By.XPATH, '//span[@class="_13fwAio4RLr1IF _20_v2t8pu5W336"][normalize-space()="Boards"]')
    board = (By.XPATH, '//div[@title="TestBoard"]//div[contains(text(),"TestBoard")]')
    create_list = (By.XPATH, '//span[@class="placeholder"]')
    list_title = (By.XPATH, '//input[@placeholder="Enter list title…"]')
    add_list = (By.XPATH, '//input[@value="Add list"]')


    @staticmethod
    def board_col(number):
        board_column = (By.XPATH, f'//div[@class="js-list list-wrapper"][{number}]')
        return board_column

    @staticmethod
    def create_card(number):
        card = (By.XPATH, f'//div[@class="js-list list-wrapper"][{number}]//a[@class="open-card-composer js-open-card-composer"]')
        return card

    @staticmethod
    def card_title(number):
        card = (By.XPATH, f'//div[@class="js-list list-wrapper"][{number}]//textarea[@class="list-card-composer-textarea js-card-title"]')
        return card

    @staticmethod
    def add_card(number):
        card = (By.XPATH, f'//div[@class="js-list list-wrapper"][{number}]//input[@class="nch-button nch-button--primary confirm mod-compact js-add-card"]')
        return card

    @staticmethod
    def card(number):
        card = (By.XPATH, f'//div[@class="js-list list-wrapper"][{number}]//a[@class="list-card js-member-droppable ui-droppable"][{number}]//div[@class="list-card-details js-card-details"]')
        return card

    board_column1 = (By.XPATH, '//div[@class="js-list list-wrapper"][1]')
    board_column2 = (By.XPATH, '//div[@class="js-list list-wrapper"][2]')
    add_card_column1 = (By.XPATH, '//div[@class="js-list list-wrapper"][1]//a[@class="open-card-composer js-open-card-composer"]')
    add_card_column2 = (By.XPATH, '//div[@class="js-list list-wrapper"][1]//a[@class="open-card-composer js-open-card-composer"]')
    # card_title1 = (By.XPATH, '//div[@class="js-list list-wrapper"][1]//textarea[@class="list-card-composer-textarea js-card-title"]')
    card_title1 = (By.XPATH, '//textarea[@placeholder="Enter a title for this card…"]')
    # add_card1 = (By.XPATH, '//div[@class="js-list list-wrapper"][1]//input[@class="nch-button nch-button--primary confirm mod-compact js-add-card"]')
    add_card1 = (By.XPATH, '//input[@value="Add card"]')
    card1 = (By.XPATH, '//div[@class="js-list list-wrapper"][1]//a[@class="list-card js-member-droppable ui-droppable"][1]//div[@class="list-card-details js-card-details"]')
    delete_card = (By.XPATH, '//span[normalize-space()="Archive"]')
    source_card = (By.XPATH, '//div[@class="js-list list-wrapper"][1]//a[@class="list-card js-member-droppable ui-droppable"][1]')
    destination_cared_list = (By.XPATH, '//div[@class="js-list list-wrapper"][2]//div[@class="list-cards u-fancy-scrollbar u-clearfix js-list-cards js-sortable ui-sortable"]')


