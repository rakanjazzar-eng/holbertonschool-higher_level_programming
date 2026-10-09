#!/usr/bin/env python3
"""Module for basic JSON serialization and deserialization."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load a JSON file and return it as a Python dictionary."""

    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
