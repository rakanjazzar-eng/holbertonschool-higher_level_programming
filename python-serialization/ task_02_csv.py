#!/usr/bin/env python3
"""Module that converts CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and write it to data.json."""
    try:
        with open(csv_filename, mode='r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as f:
            json.dump(data, f)

        return True
    except FileNotFoundError:
        return False
