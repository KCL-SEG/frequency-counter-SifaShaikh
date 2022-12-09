"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    # Your code goes here
    frequencies = {}
    for item in items:
        frequencies[str(item)] = frequencies.get(str(item), 0)+1
    return frequencies
