import types


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(arg=None):
        if cls not in instances:
            if arg is None:
                instances[cls] = cls(*args, **kw)
            else:
                instances[cls] = {}
        if arg and arg not in instances[cls]:
            instances[cls][arg] = cls(arg, *args, **kw)
        if arg is None:
            assert type(instances[cls]) is not types.DictType
            return instances[cls]
        else:
            assert type(instances[cls]) is types.DictType
            return instances[cls][arg]
    return _singleton
