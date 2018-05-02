import json
import os

class Configuration(object):

    def __init__(self, config_path='~/.confs'):
        self.config_path = os.path.expanduser(config_path)

    def load(self):
        if not os.path.exists(self.config_path):
            self.configuration = {}
            return False

        with open(self.config_path, 'r') as f:
            data = f.read()

        self.configuration = json.loads(data)
        return True

    def save(self):
        with open(self.config_path, 'w') as f:
            f.write(json.dumps(self.configuration, indent=4))

    def get_path(self):
        return self.config_path

    def get(self, path_parts, fallback=None):
        tree = self.configuration
        for part in path_parts:
            if part in tree:
                tree = tree[part]
            else:
                return fallback

        return tree

    def set(self, path_parts, value):
        tree = self.configuration
        for part in path_parts[:-1]:
            if part not in tree:
                tree[part] = {}

            tree = tree[part]
        
        tree[path_parts[-1]] = value
