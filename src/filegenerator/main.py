from typer import Typer
from filegenerator.cli import create as file_create_cli
from filegenerator.cli import list as file_list_cli

app = Typer(help="📁 File Generator CLI")

app.add_typer(file_create_cli.app)
app.add_typer(file_list_cli.app)