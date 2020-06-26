import click

from .facade import greeting, list_all_user


@click.group()
def main():
    pass

@main.command()
@click.argument('name')
def greet(name):
    click.echo(greeting(name))

@main.command()
def list_user():
    click.echo(list_all_user())