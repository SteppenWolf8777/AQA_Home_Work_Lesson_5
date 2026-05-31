import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    # Настройка конфигурации браузера
    browser.config.driver_name = "chrome"
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_size = (1920, 1080)
    browser.config.timeout = 6
    browser.config.hold_browser_open = False  # Автоматически закрывать браузер после теста

    try:
        yield
    except Exception as e:
        # Логирование ошибок (опционально)
        print(f"Тест завершился с ошибкой: {e}")
        raise
    finally:
        # Гарантированное закрытие браузера даже при ошибках
        browser.quit()