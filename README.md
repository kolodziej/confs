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

## How it works?

First of all, you need to initialize your repository. Repository has nothing in
common with git, svn or any other version control system. It is Confs'
repository of dotfiles. Inside repository you will following directories:

* \_endpoint - place where all currently used dotfiles are placed (ready to use, so
  all templates are already rendered)
* \_all - place for all configurations that are general - it means that such config
  will be available for any host
* other directories' names are reserved for hosts, so they contain dotfiles for
  reserved for specific hosts only

To initialize repository you have to call command: `confs init`. You can use
additional parameters: `--config` to point file which will contain confs
configuration and `--id` which specify your system identifier (which is located
in `~/.confsid` file). When `--id` is not specified default value is generated
using hostname and operating system type (e.g. kacper.lan\_linux).

Confs can add existing dotfiles to repository. To do it, use command: `confs add
dotfile`, where `dotfile` is relative path based in your home directory.
