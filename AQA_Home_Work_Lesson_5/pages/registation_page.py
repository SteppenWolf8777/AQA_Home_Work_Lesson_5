from selene import browser


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def user_email(self, value):
        browser.element("#userEmail").type(value)

    def user_number(self, value):
        browser.element("#userNumber").type(value)
