from selene import browser, have

from AQA_Home_Work_Lesson_5 import resources


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


def test_demo_aqa():
    reg_page = RegistrationPage()
    reg_page.open()
    reg_page.fill_first_name("Alexander")
    reg_page.fill_last_name("Python")
    reg_page.user_email("alex_python_aqa@test.com")
    reg_page.user_number("9033247777")

    browser.element('label[for="gender-radio-1"]').click()
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element('.react-datepicker__month-select option[value="11"]').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element('.react-datepicker__year-select option[value="1999"]').click()
    browser.element('[aria-label="Choose Sunday, December 5th, 1999"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element("#subjectsInput").type("com").press_enter()

    # browser.element("#uploadPicture").set_value(resourse.picture_path)
    browser.element('#uploadPicture').set_value(resources.path('test.jpg'))


    browser.element("#currentAddress").type("Саратов, Усиевича 33а")

    browser.element("#state").click()
    browser.element("#react-select-3-input").type("Haryana").press_enter()

    browser.element("#city").click()
    browser.element("#react-select-4-input").type("Karnal").press_enter()

    browser.element("#submit").click()
    browser.element("#example-modal-sizes-title-lg").should(
        have.text("Thanks for submitting the form")
    )

    browser.all(".table td:nth-child(2)").should(
        have.exact_texts(
            "Alex Python",
            "alex_python_aqa@test.com",
            "Male",
            "9033247777",
            "05 December,1999",
            "Computer Science",
            "Reading",
            "test.jpg",
            "Саратов, Усиевича 33а",
            "Haryana Karnal",
        )
    )
