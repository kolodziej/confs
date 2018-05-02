import os
import subprocess

class Endpoint(object):
    def __init__(self, repo):
        self.repo = repo
        self.endpoint_path = os.path.join(
            self.repo.get_path(),
            '_endpoint'
        )

    def create_endpoint(self):
        result = subprocess.call([
            'mkdir', '-p', self.endpoint_path
        ])

        return result == 0

    def get_path(self):
        return self.endpoint_path

    def get_file_path(self, path):
        return os.path.join(self.get_path(), path)

    def link(self, install_path):
        result = subprocess.call([
            'ln', '-sf',
            self.get_file_path(install_path),
            Endpoint.get_home_path(install_path)
        ])

        return result == 0

    @staticmethod
    def get_home_path(install_path):
        return os.path.join(
            os.path.expanduser('~'),
            install_path
        )
