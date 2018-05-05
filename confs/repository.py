import os
import subprocess

class Repository(object):
    """ Repository with configuration files """
    CONFSID_NAME = '.confsid'

    def __init__(self, path, ident):
        if path is None:
            raise Exception("Repository path cannot be null!")

        self.path = path
        self.ident = ident

    def check_if_repo_exists(self):
        path = os.path.join(self.path, Repository.CONFSID_NAME)
        return os.path.exists(path)

    def create(self):
        hosts = ['_common']
        if self.ident is not None:
            hosts.append(self.ident)

        result = subprocess.call([
            'mkdir', '-p', os.path.join(self.path, '_endpoint')
        ])

        if result != 0:
            raise Exception("Could not create endpoint for repository")

        for host in hosts:
            self.add_host(host)

        confsid_path = os.path.join(self.path, Repository.CONFSID_NAME)
        with open(confsid_path, 'w') as f:
            f.write(self.ident)

    def add_host(self, ident):
        result = subprocess.call([
            'mkdir', '-p', ident
        ])

        if result != 0:
            raise Exception("Could not create directory for host {}".format(ident))

        files = [
            os.path.join(self.path, '{}.json'.format(ident)),
            os.path.join(self.path, '{}.priv.json'.format(ident))
        ]
        result = subprocess.call([
            'touch', *files
        ])

        if result != 0:
            raise Exception("Could not create contexts for host {}".format(ident))

    def set_ident(self, ident):
        self.ident = ident

    def get_ident(self):
        if self.ident is None:
            return ''
        else:
            return self.ident.get()

    def get_path(self):
        return self.path

    def get_ident_path(self):
        return os.path.join(self.path, self.get_ident())

    def get_file_path(self, name):
        if self._has_file(name, self.get_ident()):
            return self._get_file_path(name, self.get_ident())

        if self._has_file(name):
            return self._get_file_path(name)

        return None

    def get_file_relpath(self, name):
        path = self.get_file_path(name)
        if path is None:
            return path

        return os.path.relpath(path, start=self.get_path())

    def _get_file_path(self, name, ident=None):
        path_parts = [
            self.path,
            ident if ident is not None else '',
            name
        ]

        return os.path.join(*path_parts)

    def _has_file(self, name, ident=None):
        path = self._get_file_path(name, ident)
        return os.path.exists(path)
