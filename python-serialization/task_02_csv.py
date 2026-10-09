#!/usr/bin/python3
"""Convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its rows as JSON to data.json."""
    try:
        with open(csv_filename, 'r', encoding='utf-8') as f:
            data = list(csv.DictReader(f))
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
        return True
    except Exception:
        return False
