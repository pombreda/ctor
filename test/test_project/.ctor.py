import sys
from ctor import env
from ctor.targets import Executable

main = Executable(
    output = "main",
    inputs = [
        "main.c",
        "module1",
        IF(sys.platform == "win32", "module2"),
    ],
    flags = {},
)


@CustomTarget(depends = [main])
def copy_everything():
    cp("main", "rpm/main")
    build_rpm()



