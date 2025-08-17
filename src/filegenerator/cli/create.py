import typer
from filegenerator.core.generator import generate_file, generate_csv, generate_excel

app = typer.Typer(help="🔨 Commands related to file generation.")

@app.command("cat")
def create_file(
    filename: str = typer.Argument(..., help="Name of the fiel to create"),
    format: str = typer.Option("txt", "--format", "-f", help="File format (txt, html, json, etc.)"),
    content: str = typer.Option("", "--content", "-c", help="Initial content"),
    force: bool = typer.Option(False, "--force", "-F", help="Overwrite if file exists")
    ):
    """
    Create a new file of a given format
    """
    generate_file(filename, format, content, force)

    generate_csv()
    generate_excel()