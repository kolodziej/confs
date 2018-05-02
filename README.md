# Confs

Confs is a lightweight dotfiles manager written in Python. It supports
templating configuration files for mulitple hosts. Now it requires python 3.x,
but in the future it will also be backported to Python 2.7.

## Usage

To use Confs you need to know a few simple commands:

```
confs init [path] # initialize repository
confs install dotfile [dotfile...] # install dotfile in your system
confs uninstall dotfile [dotfile...] # uninstall dotfile from your system
confs add path # add existing dotfile to repository
```

Each of this command has additional arguments which you can check calling
application with `-h` argument.
