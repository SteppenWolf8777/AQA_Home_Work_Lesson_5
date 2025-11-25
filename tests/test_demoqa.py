from pathlib import Path

from selene import browser, have


def test_demo_aqa():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Python')
    browser.element('#userEmail').type('alex_python_aqa@test.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9033247777')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1999"]').click()
    browser.element('[aria-label="Choose Sunday, December 5th, 1999"]').click()

def test_demo_aqa1():
    browser.open('/automation-practice-form')
    browser.element('#subjectsInput').type('Python').press_enter()
    browser.element('label[for="hobbies-checkbox-2"]').click()

    picture_path = str(Path(__file__).parent.parent.joinpath('Photo', "test.jpg").resolve())
    browser.element('#uploadPicture').set_value(picture_path)

    browser.element('#currentAddress').type('Саратов, Усиевича 33а')



