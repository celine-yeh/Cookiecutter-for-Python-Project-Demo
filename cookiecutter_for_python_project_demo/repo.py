from .util import lazy_service
from .db import get_session
from .model import User


class BaseRepository:
    MODEL_CLS = None

    @property
    def _session(self):
        return get_session()

    def get(self, id_):
        return self._session.query(self.MODEL_CLS).filter_by(_id=id_).one()

    def list(self):
        return self._session.query(self.MODEL_CLS).all()

    def add(self, entity):
        self._session.add(entity)
        self._session.flush()
        return entity.id

    def delete(self, id_):
        entity = self.get(id_)
        self._session.delete(entity)
        self._session.flush()


class UserRepository(BaseRepository):
    MODEL_CLS = User


@lazy_service
def user_repo():
    return UserRepository()