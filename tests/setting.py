# main.py
import json
import configparser
import os
import argparse
from collections import defaultdict
from pathlib import Path

# --- Example Configuration File Contents (Multi-Profile) ---

# config.json
# {
#     "report": {
#         "output_filename": "generated_report.txt",
#         "title": "Monthly Sales Report",
#         "author": "Admin",
#         "include_header": true,
#         "sections": ["Introduction", "Sales Data", "Conclusion"]
#     },
#     "document": {
#         "output_filename": "generated_document.md",
#         "title": "Project Documentation",
#         "author": "Dev Team",
#         "include_header": false,
#         "sections": ["Overview", "Installation", "Usage"]
#     }
# }

# config.yaml
# report:
#   output_filename: generated_report.txt
#   title: Monthly Sales Report
#   author: Admin
#   include_header: true
#   sections:
#     - Introduction
#     - Sales Data
#     - Conclusion
# document:
#   output_filename: generated_document.md
#   title: Project Documentation
#   author: Dev Team
#   include_header: false
#   sections:
#     - Overview
#     - Installation
#     - Usage

# config.ini
# [report.file_settings]
# output_filename = generated_report.txt
# include_header = yes
#
# [report.content]
# title = Monthly Sales Report
# author = Admin
# sections =
#     Introduction
#     Sales Data
#     Conclusion
#
# [document.file_settings]
# output_filename = generated_document.md
# include_header = no
#
# [document.content]
# title = Project Documentation
# author = Dev Team
# sections =
#     Overview
#     Installation
#     Usage


# --- Configuration Loading Functions ---

def load_config_json(filepath):
    """Loads all profiles from a JSON file."""
    print(f"-> Loading configuration from JSON: {filepath}")
    
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "src/filegenerator" / "config_file" / "config.json"

    print(f"{config_path} actual path here")
    try:
        with open(config_path, 'r') as f:
            
            json_data = json.load(f)
            print(f"Json data {json_data}")
            return json_data
    except FileNotFoundError:
        print(f"Error: JSON config file not found at '{filepath}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filepath}'")
        return None


def load_config_yaml(filepath):
    """Loads all profiles from a YAML file."""
    print(f"-> Loading configuration from YAML: {filepath}")
    # try:
    #     with open(filepath, 'r') as f:
    #         return yaml.safe_load(f)
    # except FileNotFoundError:
    #     print(f"Error: YAML config file not found at '{filepath}'")
    #     return None
    # except yaml.YAMLError:
    #     print(f"Error: Could not parse YAML from '{filepath}'")
    #     return None


def load_config_ini(filepath):
    """Loads all profiles from an INI file and converts to a nested dict."""
    print(f"-> Loading configuration from INI: {filepath}")
    if not os.path.exists(filepath):
        print(f"Error: INI config file not found at '{filepath}'")
        return None

    config = configparser.ConfigParser()
    config.read(filepath)
    
    profiles = defaultdict(dict)
    for section in config.sections():
        try:
            profile_name, section_type = section.split('.')
            if section_type == 'file_settings':
                profiles[profile_name]['output_filename'] = config.get(section, 'output_filename')
                profiles[profile_name]['include_header'] = config.getboolean(section, 'include_header')
            elif section_type == 'content':
                profiles[profile_name]['title'] = config.get(section, 'title')
                profiles[profile_name]['author'] = config.get(section, 'author')
                sections_str = config.get(section, 'sections')
                profiles[profile_name]['sections'] = [sec.strip() for sec in sections_str.strip().split('\n')]
        except ValueError:
            print(f"Warning: Skipping malformed section in INI file: '{section}'")

    return dict(profiles)

# --- Configuration Saving Functions ---

def save_config_json(filepath, data):
    """Saves all profiles to a JSON file."""
    print(f"-> Saving configuration to JSON: {filepath}")
    
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "src/filegenerator" / "config_file" / "config.json"
    
    try:
        with open(config_path, 'w') as f:
            json.dump(data, f, indent=4)
        print("✅ Save successful.")
    except IOError as e:
        print(f"Error writing to JSON file: {e}")

def save_config_yaml(filepath, data):
    """Saves all profiles to a YAML file."""
    print(f"-> Saving configuration to YAML: {filepath}")
    try:
        with open(filepath, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        print("✅ Save successful.")
    except IOError as e:
        print(f"Error writing to YAML file: {e}")

def save_config_ini(filepath, data):
    """Saves all profiles to an INI file."""
    print(f"-> Saving configuration to INI: {filepath}")
    config = configparser.ConfigParser()
    for profile_name, profile_data in data.items():
        config[f'{profile_name}.file_settings'] = {
            'output_filename': profile_data.get('output_filename', ''),
            'include_header': 'yes' if profile_data.get('include_header') else 'no'
        }
        config[f'{profile_name}.content'] = {
            'title': profile_data.get('title', ''),
            'author': profile_data.get('author', ''),
            'sections': '\n'.join(f"    {sec}" for sec in profile_data.get('sections', []))
        }
    try:
        with open(filepath, 'w') as f:
            config.write(f)
        print("✅ Save successful.")
    except IOError as e:
        print(f"Error writing to INI file: {e}")


# --- Core Logic ---

def generate_file(config):
    """Generates a file based on the provided configuration dictionary."""
    if not config:
        print("Configuration is missing. Cannot generate file.")
        return

    filename = config.get('output_filename', 'default_output.txt')
    title = config.get('title', 'Default Title')
    author = config.get('author', 'Unknown Author')
    include_header = config.get('include_header', False)
    sections = config.get('sections', [])

    print(f"\n--- Generating file: {filename} ---")
    try:
        with open(filename, 'w') as f:
            if include_header:
                f.write("=" * 40 + "\n")
                f.write(f"Title: {title}\n")
                f.write(f"Author: {author}\n")
                f.write("=" * 40 + "\n\n")

            f.write(f"# {title}\n\n")

            for i, section in enumerate(sections, 1):
                f.write(f"## {i}. {section}\n")
                f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\n")

        print(f"✅ Successfully created '{filename}'")
    except IOError as e:
        print(f"Error writing to file: {e}")
    print("--------------------------------------\n")

def _convert_value(value):
    """Tries to convert a string value to a more appropriate type."""
    if value.lower() == 'true': return True
    if value.lower() == 'false': return False
    try: return int(value)
    except ValueError: pass
    try: return float(value)
    except ValueError: pass
    return value

def main():
    """
    Main function to parse command-line arguments and run the generator.
    To generate a file:
        python main.py --config config.json --profile report
    To modify a config value:
        python main.py --config config.json --profile report --set author "New Author"
    """
    parser = argparse.ArgumentParser(description="A multi-profile file generator CLI.")
    parser.add_argument('--config', type=str, required=True, help="Path to the configuration file.")
    parser.add_argument('--profile', type=str, required=True, help="The configuration profile to use.")
    parser.add_argument('--set', nargs=2, metavar=('KEY', 'VALUE'), help="Set a configuration value for the profile.")
    args = parser.parse_args()
    
    config_path = args.config
    profile_name = args.profile

    # Determine file type and assign load/save functions
    if config_path.endswith('.json'):
        load_func, save_func = load_config_json, save_config_json
    elif config_path.endswith(('.yaml', '.yml')):
        load_func, save_func = load_config_yaml, save_config_yaml
    elif config_path.endswith('.ini'):
        load_func, save_func = load_config_ini, save_config_ini
    else:
        print("Error: Unsupported config file format. Use .json, .yaml, or .ini")
        return

    all_profiles = load_func(config_path)
    if all_profiles is None:
        return

    profile_data = all_profiles.get(profile_name)
    if profile_data is None:
        print(f"Error: Profile '{profile_name}' not found in '{config_path}'")
        return

    # If --set is used, modify the profile and save the entire file
    if args.set:
        key, value = args.set
        print(f"key - {key} , value - {value}")
        converted_value = _convert_value(value)
        print(f"converted value {converted_value}")
        print(f"-> Modifying profile '{profile_name}': Setting '{key}' to '{converted_value}'")
        profile_data[key] = converted_value
        all_profiles[profile_name] = profile_data # Update the main dictionary
        save_func(config_path, all_profiles)
    else:
        # Otherwise, generate the file using the selected profile
        print(f"-> Using profile: '{profile_name}'")
        generate_file(profile_data)


if __name__ == "__main__":
    main()
