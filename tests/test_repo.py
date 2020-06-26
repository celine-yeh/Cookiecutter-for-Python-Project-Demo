# pylint: disable=unused-argument
import pytest

from sqlalchemy.orm.exc import NoResultFound

from cookiecutter_for_python_project_demo.db import transaction
from cookiecutter_for_python_project_demo.repo import user_repo
from cookiecutter_for_python_project_demo.model import User


@pytest.mark.large
def test_user_repo(clean_db):
    with transaction():
        assert user_repo.list() == []

    with transaction():
        user1_id = user_repo.add(User('celine', 'Celine Yeh'))
        assert user1_id == 1
        user2_id = user_repo.add(User('antonio', 'Antonio Hong'))
        assert user2_id == 2

    with transaction():
        user_info = [
            (user.id, user.username, user.display_name)
            for user in user_repo.list()
        ]
        assert user_info == [
            (1, 'celine', 'Celine Yeh'),
            (2, 'antonio', 'Antonio Hong'),
        ]

    with transaction():
        user = user_repo.get(1)
        assert user.username == 'celine'
        assert user.display_name == 'Celine Yeh'

    with transaction():
        user_repo.delete(1)

    with transaction():
        user_info = [
            (user.id, user.username, user.display_name)
            for user in user_repo.list()
        ]
        assert user_info == [
            (2, 'antonio', 'Antonio Hong'),
        ]

    with transaction():
        with pytest.raises(NoResultFound):
            user_repo.get(1)