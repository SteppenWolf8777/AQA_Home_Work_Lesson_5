from selene import browser, have
from AQA_Home_Work_Lesson_5.pages.registation_page import RegistrationPage
from AQA_Home_Work_Lesson_5.resources import get_resource_path


def test_demo_aqa():
    reg_page = RegistrationPage()
    reg_page.open()
    reg_page.fill_first_name("Alexander")
    reg_page.fill_last_name("Python")
    reg_page.user_email("alex_python_aqa@test.com")
    reg_page.user_number("9033247777")

    browser.element('label[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("9033247777")

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element('.react-datepicker__month-select option[value="11"]').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element('.react-datepicker__year-select option[value="1999"]').click()
    browser.element('[aria-label="Choose Sunday, December 5th, 1999"]').click()

    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element("#subjectsInput").type("com").press_enter()

    browser.element('#uploadPicture').set_value(get_resource_path('test.jpg'))


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
            "Alexander Python",
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

123


4445
