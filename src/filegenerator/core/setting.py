import json
import configparser
import os
import argparse
from collections import defaultdict

import logfire
def load_config_json(filepath: str):
    """Loads all profiles from a JSON file"""
    logfire.info(f" -> Loading configuration from JSON: {filepath}")
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logfire.info(f"Error: JSON config file not found at '{filepath}'")
        return None
    except json.JSONDecodeError:
        logfire.info(f"Error: Could not decode JSON from '{filepath}'")
        return None
    
def save_config_json(filepath: str, data: str):
    """Save all profiles to a JSON file."""
    logfire.info(f"-> Saving Configuration to JSON: {filepath}")
    
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        logfire.info("Save successfully")
    except IOError as e:
        logfire.info(f"Error writing to JSON File: {e}")


    
    
    