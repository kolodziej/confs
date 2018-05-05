# Use cases

## Initialize repository

1. Check if configuration exists
3. Check if repository exists
4. If any of above exists show warning and exit (force using --force option)
5. Else create repository and save all data (config, ident, create repository
   directories)

## Install dotfile

1. Check if dotfile exists
2. If exists and is managed by confs, show proper information and exit
3. If exists but is not managed by confs, ask to use --force option
4. If doesn't exist, try to render and install

## Add dotfile to repository

1. Check if dotfile exists
2. Check if such dotfile is not available in confs repository
3. If dotfile exists and name is free in confs, add it and install
4. Else ask to overwrite (--force)

## Uninstall dotfile

1. Check if dotfile is managed by confs
2. If not, ask for (--force) option
3. Remove link from home

## Remove dotfile from repository

1. Check if dotfile exists and is installed
2. If exists and is installed, ask to use --force option
3. Else, remove
4. If force option is set and dotfile exists and is installed, uninstall it and
   remove
