import logging
import whois
import os
import json
logger = logging.getLogger()


def add_to_json_file(file_path: str, data: dict) -> None:
    """ Add data to output json file"""
    if not os.path.exists(file_path):
        # File does not exist. Dump first batch of data
        with open(file_path, 'w+') as f:
            json.dump(data, f)
    else:
        # File exists. Read existing data, append new data and dump
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
        # Dump updated data back to file
        with open(file_path, 'w+') as f:
            existing_data.update(data)
            json.dump(existing_data, f)


def is_domain_name_available(domain_name: str, total_lines: int, current_count: int) -> bool:
    """ Returns whether or not domain name is available"""
    try:
        whois.whois(domain_name)
        logger.info(f"{current_count}/{total_lines} Domain name is unavailable: {domain_name}")
        return False
    except whois.parser.PywhoisError:
        logger.info(f"{current_count}/{total_lines} Domain name is available: {domain_name}")
        return True


