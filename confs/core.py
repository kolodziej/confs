import platform
import json
import os
import sys
import subprocess
import jinja2

from .repository import Repository
from .endpoint import Endpoint
from .renderer import Renderer
from .exceptions import *

class Core(object):
    """ Core class represents core of confs app """

    def __init__(self, configuration, ident, repo):
        self.configuration = configuration
        self.ident = ident
        self.repo = repo

        self.repo.set_ident(self.ident)
        self.endpoint = Endpoint(self.repo)

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
