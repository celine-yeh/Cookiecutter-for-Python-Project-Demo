from cookiecutter_for_python_project_demo._config import Config


def test_debug():
    settings = {'debug': True}
    config = Config(settings)

    assert config.debug is True

def test_sqlalchemy_database_url():
    settings = {'mysql': {
        'host': 'db',
        'username': 'app',
        'password': 'secret',
        'database': 'app_db',
    }}
    config = Config(settings)

    assert config.sqlalchemy_database_url == \
        'mysql+pymysql://app:secret@db/app_db?charset=utf8mb4'