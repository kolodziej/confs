import sys
import click

from confs import Core, Repository, Configuration, Ident, Endpoint

@click.group()
@click.option('--config', default='~/.confsrc', help='Confs configuration file')
@click.option('--id', default=None, help='id')
@click.pass_context
def main(ctx, config, id):
    ctx.obj = {
        'config': config,
        'id': id,
    }

@main.command()
@click.argument('directory', default='~/confs/')
@click.pass_context
def init(ctx, directory):
    configuration = Configuration(ctx.obj['config'])
    ident = Ident(ctx.obj['id'])

    if configuration.load():
        print("WARNING: Configuration has already been created!")

    try:
        repo = Repository(directory, ident)
        if not repo.create_repository():
            raise Exception("Could not create directory for repository!")

        endpoint = Endpoint(repo)
        if not endpoint.create_endpoint():
            raise Exception("Could not create directory for endpoint!")

        configuration.set([ident.get(), 'repo'], directory)
    except Exception as exc:
        print("Error: {}".format(str(exc)))
        sys.exit(1)

    configuration.save()

@main.command()
@click.argument('dotfile', required=True, nargs=-1)
@click.pass_context
def install(ctx, dotfile):
    configuration = Configuration(ctx.obj['config'])
    configuration.load()

    ident = Ident(ctx.obj['id'])
    repository = Repository(configuration.get([ident.get(), 'repo']), ident)
    core = Core(configuration, ident, repository)

    try:
        for f in dotfile:
            core.install(f)
    except Exception as exc:
        print("Error: {}".format(str(exc)))
        exc.traceback()

@main.command()
@click.argument('dotfile', required=True, nargs=-1)
@click.option('--remove', help='Remove from endpoint', is_flag=True)
@click.pass_context
def uninstall(ctx, dotfile, remove):
    configuration = Configuration(ctx.obj['config'])
    configuration.load()

    ident = Ident(ctx.obj['id'])
    repository = Repository(configuration.get([ident.get(), 'repo']), ident)
    core = Core(configuration, ident, repository)

    try:
        for f in dotfile:
            core.uninstall(f)
    except Exception as exc:
        print("Error: {}".format(str(exc)))
        exc.traceback()

@main.command()
@click.argument('dotfile', required=True)
@click.option('--only-this-id', help='Only for this system?', is_flag=True)
@click.pass_context
def add(ctx, dotfile, only_this_id):
    configuration = Configuration(ctx.obj['config'])
    configuration.load()

    ident = Ident(ctx.obj['id'])
    repository = Repository(configuration.get([ident.get(), 'repo']), ident)
    core = Core(configuration, ident, repository)

    try:
        core.add(dotfile, only_this_id)
    except Exception as exc:
        print("Error: {}".format(str(exc)))
        exc.traceback()
    

if __name__ == '__main__':
    main()
