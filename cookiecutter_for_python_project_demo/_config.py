import os
import yaml

from .util import lazy_service


class Config:

    def __init__(self, settings):
        self._settings = settings

    @property
    def debug(self):
        return self._settings.get('debug')

    @property
    def sqlalchemy_database_url(self):
        return 'mysql+pymysql://%(username)s:%(password)s' \
               '@%(host)s/%(database)s?charset=utf8mb4' \
               % self._settings['mysql']


@lazy_service
def config():
    with open(os.environ['SETTINGS_PATH']) as ymlfile:
        settings = yaml.load(ymlfile, Loader=yaml.FullLoader)

    return Config(settings)
