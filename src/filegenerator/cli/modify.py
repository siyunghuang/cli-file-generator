import typer
import logfire
import json

from pathlib import Path

app = typer.Typer(help="Commands related to modify file generation settings")

@app.command("m")
def modify_file_settings():
    logfire.info(f"Modifying file settings")
    
    directory_parent = Path(__file__).resolve().parent.parent
    json_config_path = directory_parent / "file_config" / "file_settings.json"
    logfire.info(f"Directory parent path {directory_parent}")
    
    try:
        with open(json_config_path, 'r') as f:
            json_data = json.load(f)
            logfire.info(f"Json Data {json_data}")
    except FileNotFoundError:
        logfire.error(f"ERROR: JSON config file not found at {json_config_path}")
    except json.JSONDecodeError:
        logfire.error(f"ERROR: Could not decode JSON from {json_config_path}")
