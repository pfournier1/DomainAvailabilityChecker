import logging
import whois
import os
import json
logger = logging.getLogger()


def is_domain_available(domain_name: str, total_lines: int, current_count: int) -> bool:
    try:
        domain = whois.query(domain_name)
    except Exception as e:
        logger.warning(f"{current_count}/{total_lines} Checking domain failed: {domain_name}")
        logger.warning(e)
        return False
    if domain:
        logger.info(f"{current_count}/{total_lines} Domain is unavailable: {domain_name}")
        return False
    else:
        logger.info(f"{current_count}/{total_lines} Domain is available: {domain_name}")
        return True


def add_to_json_file(file_path: str, data: dict) -> None:
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
