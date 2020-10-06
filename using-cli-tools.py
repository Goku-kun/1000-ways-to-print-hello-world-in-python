import click

@click.command()
@click.option('--count', default=1, help='number of hello worlds!')
def hello(count):
    for x in range(count):
        click.echo('Hello, world!')

if __name__ == "__main__":
    hello()