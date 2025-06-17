import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.window_width = 1366
    browser.config.window_height = 705
    yield
    browser.quit()