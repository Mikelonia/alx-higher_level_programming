#!/usr/bin/python3
# 11-student.py
"""Defining a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Getting a dictionary representation of the Student."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
