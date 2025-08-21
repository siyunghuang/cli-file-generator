from typer import Typer
from filegenerator.cli import create as file_create_cli
from filegenerator.cli import list as file_list_cli
from filegenerator.cli import view as file_view_cli
from filegenerator.cli import modify as file_modify_cli

from filegenerator.cli_config.config import settings

import logfire

logfire.configure(
    token=settings.LOGFIRE_TOKEN,
    service_name=settings.PROJECT_NAME,
    service_version=settings.VERSION,
    environment=settings.ENV,
    console=False)

logfire.info("Running CLI")
app = Typer(help="📁 File Generator CLI")
app.add_typer(file_create_cli.app)
app.add_typer(file_list_cli.app)
app.add_typer(file_view_cli.app)
app.add_typer(file_modify_cli.app)