from pathlib import Path

import typer
import pandas as pd
from rich.progress import track

from pydantic import ValidationError
from filegenerator.core.types import User
from importlib.resources import files

def generate_file(
        filename: str,
        format: str,
        content: str = "",
        force: bool = False
):
    path = Path(filename)

    if path.exists() and not force:
        typer.echo(f"❌ File '{filename}' already exists. Use --force to overwrite.")
        raise typer.Exit(code=1)
    
    if not path.suffix:
        path = path.with_suffix(f".{format}")

    try:
        path.write_text(content)
        typer.echo(f"✅ File '{path.name}' created successfully.")
    except Exception as e:
        typer.echo(f"❌ Failed to create file: {e}")
        raise typer.Exit(code=1)
    
def generate_csv():

    csv_path = files("filegenerator.templates").joinpath("users.csv")
    df = pd.read_csv(csv_path)
    users = []

    for value in track(range(100), description="Generating..."):
        for i, row in df.iterrows():
            try:
                user = User(**row.to_dict())
                users.append(user)
            except ValidationError as e:
                print(f"Row (i) is invalid: {e}")

        validated_df = pd.DataFrame([u.dict() for u in users])
        validated_df.to_csv("validated_users.csv", index=False)

    typer.echo(f"✅ Csv File created successfully.")

def generate_excel():

    csv_path = files("filegenerator.templates").joinpath("users.csv")
    df = pd.read_csv(csv_path)
    users = []

    for i, row in df.iterrows():
        try:
            user = User(**row.to_dict())
            users.append(user)
        except ValidationError as e:
            print(f"Row (i) is invalid: {e}")

    validated_df = pd.DataFrame([u.dict() for u in users])
    validated_df.to_excel("validated_users.xlsx", index=False)