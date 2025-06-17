import allure
from allure_commons.types import Severity
from model.issues_page import Issue_page



@allure.tag("Github")
@allure.severity(Severity.CRITICAL)
@allure.label("owner","Maksim")
@allure.feature("Задачи в репозитории")
@allure.story("Название репозитория содержит правильный заголовок")
@allure.link("https://github.com", name="Testing")
@allure.title('Тест Github steps')
def test_github_steps():
    issue = Issue_page()
    issue.open_page('https://github.com')
    issue.go_to_repo('Maks747/qa_guru_python_20_hw_10')
    issue.go_to_issue('Issue for HomeWork10')
    issue.assert_tittle_text('Issue for HomeWork10')
def test_allure_labels():
    pass