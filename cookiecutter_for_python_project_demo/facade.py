from .db import transaction
from .repo import user_repo


@transaction()
def list_all_user():
    users = user_repo.list()
    return [(user.id, user.username, user.display_name) for user in users]

def greeting(name):
    return f'Hello, {name}'
