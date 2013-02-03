class Namespace(object):
    def __getattr__(self, name):
        obj = Namespace()
        setattr(self, name, obj)
        return obj
    def __bool__(self):
        return bool(self.__dict__)
    __nonzero__ = __bool__


