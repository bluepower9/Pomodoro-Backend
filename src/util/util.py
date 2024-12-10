import json
import logging

logging.basicConfig(level = logging.INFO)

def read_configs(filename='configs.json') -> dict:
    data = None
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

    except Exception as e:
        logging.error(f'Error reading config file: {filename} - Exception: {str(e)}')
    
    return data