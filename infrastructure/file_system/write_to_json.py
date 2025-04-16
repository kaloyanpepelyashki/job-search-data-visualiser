import logging
import json

def write_to_json(file_path, data_to_write):
    logger = logging.getLogger(__name__)
    try:
        with open(file_path, "w") as file:
            if hasattr(data_to_write, "to_json"):
                file.write(data_to_write.to_json())
            else:
                json.dump(data_to_write, file, indent=4)

    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f"Error writing to file: {type(ex)}, {ex.args}")