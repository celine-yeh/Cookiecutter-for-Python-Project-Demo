import os
import yaml

from .util import lazy_service


class Config:

    def __init__(self, settings, env):
        self._settings = settings
        self._env = env

    @property
    def sqlalchemy_database_url(self):
        return 'mysql+pymysql://%(username)s:%(password)s' \
               '@%(host)s/%(database)s?charset=utf8mb4' \
               % self._settings['mysql']


@lazy_service
def config():
    env = os.environ
    with open(env['SETTINGS_PATH']) as ymlfile:
        settings = yaml.load(ymlfile, Loader=yaml.FullLoader)

    return Config(settings, env)