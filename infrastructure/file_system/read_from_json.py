import logging
import json

def read_from_json(file_path) :
    logger = logging.getLogger(__name__)
    try:
        with open(file_path, "r") as file:
            file.seek(0)
            data = json.load(file)
            return data

    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f"Error reading file: {type(ex)}, {ex.args}")