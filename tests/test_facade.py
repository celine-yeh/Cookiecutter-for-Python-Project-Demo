from cookiecutter_for_python_project_demo import facade


def test_greeting():
    assert facade.greeting('Celine') == 'Hello, Celine'
