import logging
import os
from pathlib import Path

import click
import sys
import datetime
from random import randint
from time import sleep
from config import DOMAIN_EXTENSIONS, JSON_PATH, WORDS_PATH
from helper import is_domain_available, add_to_json_file


@click.command()
@click.option('--start_index', default=0, help='Number of greetings.')
def main(start_index):
    """
    Check the availability of domains in words.txt file using each of the DOMAIN_EXTENSIONS in the config.py file
    @param: start_index: Program will run from Xth word in word file to the end. Use when whoisquery server blocks
    you and crashes program
    """
    # Create log directory
    os.makedirs(Path(__file__).parent / '../logs', exist_ok=True)
    # Configure logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    date = datetime.datetime.now().replace(microsecond=0)
    output_file_handler = logging.FileHandler(f"logs/output-{date}.log")
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(output_file_handler)
    logger.addHandler(stdout_handler)
    # Read .txt file with words
    with open(WORDS_PATH, 'r') as f:
        words = [line.replace('\n', '').lower() for line in f.readlines()]
    total_lines = len(words)
    current_count = start_index
    # For every word in the file starting at the Xth word indicated by start_index,
    # check if domain is available given different DOMAIN_EXTENSIONS
    for word in words[start_index:]:
        domain_data = {word: []}
        for domain_extension in DOMAIN_EXTENSIONS:
            domain_name = f"{word}{domain_extension}"
            is_available = is_domain_available(domain_name, total_lines, current_count)
            if is_available:
                domain_data[word].append(domain_name)
            current_count += 1
            sleep(randint(5, 10))
        if len(domain_data[word]) != 0:
            add_to_json_file(JSON_PATH, domain_data)

    logger.info('Finished')

if __name__ == '__main__':
    main()
