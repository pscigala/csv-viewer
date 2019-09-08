import click

from csvData import CSVData


def edit(txt):
    """Opens an editor with some text in it."""
    message = click.edit(txt)
    if message is not None:
        click.echo('Edited:\n' + message)
    else:
        click.echo('You did not enter anything!')


def menu(txt):
    """Shows a simple menu."""
    menu = 'main'
    while 1:
        if menu == 'main':
            click.echo('Menu:')
            click.echo('  e: edit')
            click.echo('  q: quit')
            char = click.getchar()
            if char == 'e':
                menu = 'edit'
            elif char == 'q':
                menu = 'quit'
            else:
                click.echo('Invalid input')
        elif menu == 'edit':
            click.echo('Edit')
            edit(txt)
            click.echo('  q: quit')
            char = click.getchar()
            if char == 'q':
                menu = 'quit'
            else:
                click.echo('Invalid input')
        elif menu == 'quit':
            return


@click.command()
@click.argument("file")
@click.option("-i", help="Interactive mode", is_flag=True)
@click.option("--encoding", help="File encoding", default='utf-8', show_default=True)
@click.option("--delimiter", help="Delimiter", default=';', show_default=True)
@click.option("--quotechar", help="Quotechar", default='"', show_default=True)
@click.option("--cols", help="Columns to display")
def csv_view(file, encoding, delimiter, quotechar, cols, i):
    """
    Simple CLI CSV file viewer
    """
    if file is None:
        click.echo('File is required!')
    if file is not None:
        csv = CSVData(file, encoding, delimiter, quotechar)
        txt = csv.pretty_print()
        click.echo(txt)
        if i:
            menu(txt)


if __name__ == '__main__':
    csv_view()
