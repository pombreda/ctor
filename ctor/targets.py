class BaseTarget(object):
    def __init__(self, output, inputs):
        self.output = output
        self.inputs = inputs
    def get_deps(self):
        return ()
    def get_signature(self):
        raise NotImplementedError()

class ObjectFile(BaseTarget):
    pass

class Executable(BaseTarget):
    pass

class SharedLib(BaseTarget):
    pass

class StaticLib(BaseTarget):
    pass

class JavaClass(BaseTarget):
    pass

class Jar(BaseTarget):
    pass

class CythonModule(BaseTarget):
    pass

class PythonExtensionModule(BaseTarget):
    pass















