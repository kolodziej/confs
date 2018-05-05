import platform
import json
import os
import sys
import subprocess
import jinja2

from .configuration import Configuration
from .ident import Ident
from .repository import Repository
from .endpoint import Endpoint
from .renderer import Renderer
from .exceptions import *

class Core(object):
    """ Core class represents core of confs app """

    def __init__(self):
        self.configuration = None
        self.ident = None
        self.repo = None

    def configuration_exists(self, path):
        path = os.path.expanduser(path)
        return os.path.exists(path)

    def remove_configuration(self, path):
        result = subprocess.call([
            'rm', '-f', os.path.expanduser(path)
        ])

        return result == 0

    def load_configuration(self, path):
        self.configuration = Configuration(path)
        return self.configuration.load()

    def save_configuration(self):
        self.configuration.save()

    def repository_path_exists(self):
        exists = os.path.exists(Repository.CONFS_REPOPATH)
        islink = os.path.islink(Repository.CONFS_REPOPATH)
        return exists and islink

    def set_repository_path(self, directory):
        result = subprocess.call([
            'ln', '-sf',
            os.path.userexpand(directory),
            Repository.CONFS_REPOPATH
        ])

        return result == 0

    def create_repository(self, directory):
        if self.configuration is None:
            raise Exception("Configuration has not been created!")

        if self.ident is None:
            raise Exception("Ident has not been loaded!")
        
        self.repo = Repository(directory, self.ident)
        if not self.repo.create_repository():
            raise Exception("Could not create repository!")

        conf_path = [self.ident.get(), 'repo']
        self.configuration.set(conf_path, directory)

    def ident_exists(self):
        return os.path.exists(Ident.CONFSID_PATH)

    def load_ident(self):
        self.ident = Ident()

    def set_ident(self, ident):
        self.ident = Ident(ident)

    def save_ident(self):
        self.ident.save()

    def install(self, dotfile, install_path=None):
        if self.repo.get_file_path(dotfile) is None:
            print("There is no such file: {}".format(dotfile))# change into exceptions
            sys.exit(2)

        renderer = Renderer(self.repo, self.endpoint)
        if install_path is None:
            install_path = dotfile

        context = self.configuration.get(
            [self.ident.get(), 'context'],
            {}
        )
        context = self.extend_context(context)

        renderer.render(dotfile, install_path, context)

        if not self.endpoint.link(install_path):
            raise Exception("Could not link to endpoint!")

    def uninstall(self, dotfile):
        if self.repo.get_file_path(dotfile) is None:
            print("This dotfile is not managed by Confs!") # change into exceptions
            sys.exit(2)

        result = subprocess.call([
            'rm', '-f', Endpoint.get_home_path(dotfile)
        ])

        if result != 0:
            print("Could not remove link to dotfile!")# change into exceptions
            sys.exit(2)
    
    def add(self, dotfile, only_this_system=False):
        if only_this_system:
            dstpath = self.repo.get_ident_path()
        else:
            dstpath = self.repo.get_path()

        result = subprocess.call([
            'mv', Endpoint.get_home_path(dotfile), dstpath
        ])

        if result != 0:
            raise Exception("Could not move dotfile to repository!")

        self.install(dotfile)

    def extend_context(self, context):
        new_context = {
            'hostname': platform.node()
        }

        new_context.update(context)
        return new_context
