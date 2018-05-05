import sys
import os
import click

from confs import Core, Repository, Configuration, Ident, Endpoint

@click.group()
@click.option('--force', help='Force action', is_flag=True)
@click.pass_context
def main(ctx, force):
    ctx.obj = {
        'force': force
    }

@main.command()
@click.argument('directory', default='.')
@click.argument('identifier', default=Ident.get_default())
@click.pass_context
def init(ctx, directory, identifier):
    try:
        path = os.path.join(os.getcwd(), directory)
        repo = Repository(path, identifier)
        if repo.check_if_repo_exists():
            print("ERROR: Repository already exists!")
            sys.exit(2)

        repo.create()
    except Exception as exc:
        print("error: {}".format(str(exc)))
        sys.exit(2)

@main.command()
@click.argument('dotfile', required=True, nargs=-1)
@click.pass_context
def install(ctx, dotfile):
    pass

@main.command()
@click.argument('dotfile', required=True, nargs=-1)
@click.option('--remove', help='Remove from endpoint', is_flag=True)
@click.pass_context
def uninstall(ctx, dotfile, remove):
    pass

@main.command()
@click.argument('dotfile', required=True)
@click.option('--only-this-id', help='Only for this system?', is_flag=True)
@click.pass_context
def add(ctx, dotfile, only_this_id):
    pass

if __name__ == '__main__':
    main()
