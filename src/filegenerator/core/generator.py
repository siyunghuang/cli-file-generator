from pathlib import Path

import typer
import pandas as pd

from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import time 

from rich.progress import track, Progress, SpinnerColumn, TextColumn
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
    
def generate_csv(
        filename: str,
        format: str,
        force: bool = False
):

    csv_path = files("filegenerator.templates").joinpath("users.csv")
    df = pd.read_csv(str(csv_path))
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

    typer.echo(f"✅ CSV File created successfully.")

def generate_row(i: int) -> dict:
    return {
        "ID": i,
        "Name": random.choice(["Alice, Bob", "Charlie"]),
        "Age": random.randint(20,50),
        "City": random.choice(["KL","Penang","JB"])
    }

def generate_excel(
        filename: str,
        format: str,
        force: bool = False
):
    
    start_time = time.time
    count = 1000000
    data =  [
            {
                "Name": ["Alice", "Bob", "Charlie"],
                "Age": [25, 30, 35],
                "City": ["KL", "Penang", "JB"]
            }
        ]
    
    rows = []

    # for value in track(range(100), description="Generating..."):
    with ThreadPoolExecutor(max_workers=300) as executor:
        futures = [executor.submit(generate_row, i) for i in range(count)]

        for future in track(as_completed(futures), total=len(futures), description="Generating..."):
            rows.append(future.result())
    
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Preparing an Excel File...", total=None)
        
        df = pd.DataFrame(rows)
        df.to_excel("output.xlsx", 
                    index=False, 
                    header=False, 
                    engine="xlsxwriter")

    end_time = time.time

    print("{end_time - start_time:.2f}")
    typer.echo(f"✅ XLSX File created successfully in")
