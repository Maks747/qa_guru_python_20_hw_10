from selene import browser
from selene import by, have
import allure
from allure_commons.types import Severity

@allure.title('Тест Github lambda')
def test_github_lambda():
    allure.dynamic.tag('github')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature('Tест раздела Issues')
    allure.dynamic.story('Название раздела содержит текст Issue for HomeWork10')
    allure.dynamic.link("https://github.com", name="Тест репозитория")

    with allure.step('Открыть Github'):
        browser.open('https://github.com')

    with allure.step('Перейти в репозиторий qa_guru_python_20_hw_10'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('Maks747/qa_guru_python_20_hw_10').press_enter()
        browser.element(by.link_text('Maks747/qa_guru_python_20_hw_10')).click()

    with allure.step('Проверить раздел Issue for HomeWork10'):
        browser.element('#issues-tab').click()
        browser.element(by.text('Issue for HomeWork10')).click()

    with allure.step('Проверить название раздела'):
        browser.element('[data-testid=issue-pr-title-link]').should(have.text('Issue for HomeWork10'))