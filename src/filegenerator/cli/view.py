import typer

from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel

app = typer.Typer(help="View Related Information on the CLI")

layout = Layout()
console = Console()

@app.command("dtl")
def view_file_settings():
    """
    To view detailed file setting
    """
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )

    layout["lower"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )

    layout["right"].split_row(
        Layout(Panel("Columns")),
        Layout(Panel("Headers"))
    )

    layout["left"].update(
        "The mystery of life isn't a problem to solve"
    )

    layout["upper"].size = 5

    console.print(layout)

    console.print(layout.tree)

    