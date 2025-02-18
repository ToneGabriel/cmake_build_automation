import json


__all__ = ["validate_json_data_structure", "get_json_data"]


class InvalidJsonStructure(Exception):
    """Exception raised for invalid json file structure"""

    def __init__(self: object, message: str):
        super().__init__(message)

def get_json_data(json_data_path: str, expected_structure:dict) -> dict:
    try:
        with open(json_data_path, "r") as file:
            json_data = json.load(file)
            if not validate_json_data_structure(json_data, expected_structure):
                return
            else:
                return json_data
    except FileNotFoundError:
        print(f"Error: File '{json_data_path}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{json_data_path}' is not a valid JSON file.")
        return
    except InvalidJsonStructure as e:
        print(e)
        return

def validate_json_data_structure(json_data:dict, expected_structure:dict, path="") -> bool:
    """
    Recursively validate a JSON object against the expected structure.

    :param json_data: The parsed JSON dictionary.
    :param expected_structure: The expected structure with types.
    :param path: Keeps track of the nested path for better error reporting.
    :return: True if valid, False otherwise.
    """

    if not isinstance(json_data, dict):
        print(f"Error: Expected a dictionary at '{path}', but got {type(json_data).__name__}")
        return False

    for key, expected_type in expected_structure.items():
        current_path = f"{path}.{key}" if path else key  # Track the nested key

        if key not in json_data:
            print(f"Missing key: '{current_path}'")
            return False

        if isinstance(expected_type, dict):  # Recurse for nested structures
            return validate_json_data_structure(json_data[key], expected_type, current_path)
        else:  # Validate primitive types
            if not isinstance(json_data[key], expected_type):
                print(f"Incorrect type for '{current_path}': Expected {expected_type.__name__}, got {type(json_data[key]).__name__}")
                return False

    return True
