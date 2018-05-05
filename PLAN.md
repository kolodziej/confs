# Features

1. One user can use many independent confs repositories.
2. Repository is a directory which contains file confsid which tells application
   what is id of current system for this repository.
3. init command should create new directory with basic structure:
    repo
     - .confs
     - .confsid
     - _common
     - _common.json
     - _common.priv.json
     - _endpoint
     - .gitignore
     - .bzrignore
     - .hgignore

4. Ignored files:
 - \*.priv.json
 - .confsid
 - \_endpoint

5. All commands must be run in repo directory

Repository:
    - confsid
    - add host (create host directory and two json files)
    - install (--id - force using given host)
    - uninstall
    - add (--id - force adding to given host)
    - remove host file

