import typer
from filegenerator.core.generator import generate_file, generate_csv, generate_excel
from filegenerator.constant.extension import FileFormat

app = typer.Typer(help="🔨 Commands related to file generation.")

@app.command("cat")
def create_file(
    filename: str = typer.Argument(..., help="Name of the file to create"),
    format: str = typer.Option("txt", "--format", "-f", help="File format (txt, html, json, etc.)"),
    force: bool = typer.Option(False, "--force", "-F", help="Overwrite if file exists")
    ):
    """
    Create a new file of a given format
    """

    if(format is FileFormat.FILE_FORMAT_CSV.value):
        generate_csv(filename, format, force)

    if(format is FileFormat.FILE_FORMAT_TXT.value):
        generate_excel(filename, format, force)

    if(format is FileFormat.FILE_FORMAT_XLSX.value):
        generate_excel(filename, format, force)