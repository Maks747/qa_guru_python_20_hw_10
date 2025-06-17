from selene import browser
from selene import by, have

def test_github_simple():

    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('Maks747/qa_guru_python_20_hw_10').press_enter()
    browser.element(by.link_text('Maks747/qa_guru_python_20_hw_10')).click()
    browser.element('#issues-tab').click()
    browser.element(by.text('Issue for HomeWork10')).click()

    browser.element('[data-testid=issue-pr-title-link]').should(have.text('Issue for HomeWork10'))