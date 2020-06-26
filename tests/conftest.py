
import pytest

from cookiecutter_for_python_project_demo.db import get_engine
from cookiecutter_for_python_project_demo.model import Base


@pytest.fixture
def clean_db():
    engine = get_engine()
    for table in Base.metadata.sorted_tables:
        engine.execute('TRUNCATE TABLE %s;' % table)

    return engine