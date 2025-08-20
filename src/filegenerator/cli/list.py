from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from filegenerator.core.types import available_file_types
import typer

app = typer.Typer(help="Commands related to available file types for generation")

console = Console()

@app.command("ls")
def list_file_types():
    """
    Display the avaialble file types that can be generated
    """
    table = Table(title="Available File Types")

    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Description", style="green")
    table.add_column("Setting", style="blue" )
    table.add_column("Convention", style="magenta")

    for file_type in available_file_types:
        table.add_row(file_type.name, file_type.description, file_type.settings, file_type.convention)

    panel = Panel.fit(table, title="📁 File Generator", subtitle="Use 'filegen file cat --format TYPE'", border_style="blue")
    console.print(panel)

@app.command("v")
def view_file_settings():
    """
    To view customized file settings
    """

    table = Table(title="Configured Settings")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Settings", style="green")
    table.add_column("Command", style="magenta")

    for file_type in available_settings:
        table.add_row(file_type.type, file_type.settings, file_type.command)

    panel = Panel.fit(table, title="📁 File Generator", subtitle="Use 'filegen file cat --format TYPE'", border_style="blue")
    console.print(panel)