from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    _id = Column('id', Integer, primary_key=True)
    _username = Column('username', String(16), nullable=False)
    _display_name = Column('display_name', String(20), nullable=False)

    def __init__(self, username, display_name):
        self._username = username
        self._display_name = display_name

    @hybrid_property
    def id(self):  # pylint: disable=invalid-name
        return self._id

    @hybrid_property
    def username(self):
        return self._username

    @hybrid_property
    def display_name(self):
        return self._display_name