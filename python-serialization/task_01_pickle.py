#!/usr/bin/env python3
"""Module that serializes and deserializes a custom object with pickle."""
import pickle


class CustomObject:
    """A custom object with name, age and student status."""

    def __init__(self, name, age, is_student):
        """Initialize the object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file."""
        try:
            with open(filename, mode='wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a file."""
        try:
            with open(filename, mode='rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None
