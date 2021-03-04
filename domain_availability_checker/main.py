import logging
import os
import sys
import json
import datetime
from random import randint
from time import sleep
from pathlib import Path
from typing import List, Dict
from config import DOMAIN_EXTENSIONS
from helper import is_domain_available

path = Path(__file__).parent / '../words.txt'

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    date = datetime.datetime.now().replace(microsecond=0)
    output_file_handler = logging.FileHandler(f"logs/output-{date}.log")
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(output_file_handler)
    logger.addHandler(stdout_handler)

    available_domains: Dict[str, str] = {}

    with open(path, 'r') as f:
        words = [line.replace('\n', '').lower() for line in f.readlines()]
    total_lines = len(words)
    current_count = 1

    #TODO REMOVE
    words = ["hello", "fkdfdofkw"]
    for word in words:
        for domain_extension in DOMAIN_EXTENSIONS:
            domain_name = f"{word}{domain_extension}"
            is_available = is_domain_available(domain_name, total_lines, current_count)
            if is_available:
                available_domains.setdefault(word, []).append(domain_name)
                current_count += 1
            sleep(randint(1, 2))

    logger.info('Finished')

    with open('available_domains.txt', 'w+') as f:
        json.dump(available_domains, f)


if __name__ == '__main__':
    main()
