import click


@click.group(short_help="sdftheme CLI.")
def sdftheme():
    """sdftheme CLI.
    """
    pass


@sdftheme.command()
@click.argument("name", default="sdftheme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [sdftheme]
