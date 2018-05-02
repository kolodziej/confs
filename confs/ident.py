import os
import platform

class Ident(object):
    CONFSID_PATH = os.path.expanduser('~/.confsid')

    def __init__(self, ident=None):
        self.ident = ident

        if self.ident is None:
            if not self.load():
                self.ident = Ident.get_default()
                self.save()

    def get(self):
        return self.ident

    def set(self, ident):
        self.ident = ident

    def save(self):
        with open(Ident.CONFSID_PATH, 'w') as f:
            f.write(self.ident)

    def file_exists(self):
        return os.path.exists(Ident.CONFSID_PATH)

    def load(self):
        if self.file_exists():
            with open(Ident.CONFSID_PATH, 'r') as f:
                lines = f.readlines()

            if len(lines) >= 1:
                self.ident = lines[0].strip()
                return True

        return False

    @staticmethod
    def get_default():
        identifier = '{hostname}_{os}'
        return identifier.format(
            hostname=platform.node(),
            os=platform.system().lower()
        )
