from plumbum import cli, local
from ctor.engine import CtorRootNotFound


class CtorMain(cli.Application):
    def _locate_root_dir(self):
        ctor_root_dir = local.cwd
        while not (ctor_root_dir / ".ctor.py").exists():
            if ctor_root_dir == ctor_root_dir.up():
                raise CtorRootNotFound("Unable to find .ctor.py in any parent of %s" % (local.cwd,))
            ctor_root_dir = ctor_root_dir.up()
    
    def main(self):
        self.root = self._locate_root_dir()



if __name__ == "__main__":
    CtorMain.run()
