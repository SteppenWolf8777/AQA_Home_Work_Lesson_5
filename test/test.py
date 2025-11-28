from selene import browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

browser.config.driver_name = "chrome"
browser.config.base_url = "https://todomvc.com/"
browser.config.window_width = 1920
browser.config.window_height = 1080
browser.config.timeout = 10  # Увеличьте таймаут

# Явное указание сервиса (опционально)
service = Service(ChromeDriverManager().install())

def test_demo_aqa():
    browser.open('https://todomvc.com/')
    browser.quit()