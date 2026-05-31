from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".search-input").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-testops-utils")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-testops-utils")).click()

    s("#issues-tab").click()

    s(by.partial_text("#20")).should(be.visible)
