class Proxy:

    def __init__(self, factory):
        self._factory = factory
        self._target = None

    def __getattr__(self, attr):
        if not self._target:
            self._target = self._factory()
        return getattr(self._target, attr)


def lazy_service(factory):
    return Proxy(factory)