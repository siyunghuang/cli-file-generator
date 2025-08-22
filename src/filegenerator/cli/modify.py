import typer
import logfire
import json

from pathlib import Path
from filegenerator.core.file_setting_types import ConfigModel

from typing_extensions import Annotated
from typing import Tuple

app = typer.Typer(help="Commands related to modify file generation settings")

@app.command("m")
def modify_file_settings(
    profile: Annotated[str, typer.Argument()],
    setting: Annotated[Tuple[str, int, bool], typer.Option()] = (None, None, None)
    ):
    data_type, data_size, randomize = setting
    logfire.info(f"Modifying file settings data_type {data_type} data_size {data_size} randomize {randomize}")
    
    directory_parent = Path(__file__).resolve().parent.parent
    json_config_path = directory_parent / "file_config" / "file_settings.json"
    logfire.info(f"Directory parent path {directory_parent}")
    
    try:
        with open(json_config_path, "r") as f:
            json_data = json.load(f)
            dump_json_data = json.dumps(json_data, separators=(",", ":"))
            
            logfire.info(f"Json Data {json_data}")
            logfire.info(f"[DUMP] Json Data {dump_json_data}")
            
            config = ConfigModel.model_validate_json(str(dump_json_data))
            
            
            for config_dict in config.profiles:
                if "profileA" in config_dict:
                    profile = config_dict["profileA"]
                    profile.format = "txt"
                    logfire.info(f"Selected profile {profile}") 
            
            logfire.info(f'Config {config}')
            logfire.info(f'Config {config.profiles}')
            logfire.info(f"Profile Config {config.profiles}")
            
            json_string = config.model_dump_json()
            json_string_dump = json.dumps(json_string, separators=(",", ":"))
            logfire.info(f"Reverted Json String {json_string}")
            logfire.info(f"Reverted Json String Dump {json_string_dump}")
            
            target_directory = Path(__file__).resolve().parent.parent
            target_json_config_path = target_directory / "file_config" / "target_json_config_path.json"
            
            try:
                with open(target_json_config_path, 'w') as f:
                    formatted_string = json.loads(json_string)
                    json.dump(formatted_string, f, indent=1)
            except IOError as e:
                logfire.error(f"Error writing to JSON file")
    except FileNotFoundError:
        logfire.error(f"ERROR: JSON config file not found at {json_config_path}")
    except json.JSONDecodeError:
        logfire.error(f"ERROR: Could not decode JSON from {json_config_path}")
