#!/usr/bin/python3
"""Tests for the AirBnb clone modules."""
from models.engine.file_storage import FileStorage
from typing import TextIO
import os


def clear_stream(stream: TextIO):
    """clears the contents of a given stream
    Args:
        stream (TextIO): the stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str):
    """Removes a file if it exists
    Args:
        file_path (str): The name of the file to remove.
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path='file.json'):
    """Reset the items in the given store.
    Args:
        store (FileStorage): The FileStorage to reset.
        file_path (str): The path to the store's file.
    """
    with open(file_path, mode='w') as file:
        file.write('{}')
        if store is not None:
            store.reload()


def read_text_file(file_name):
    """Reads the contents of a given file
    Args:
        file_name (str): The name of the file to read.
    Returns:
        str: The contents of the file if it exists
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                line.append(line)
    return ''.join(lines)


def write_text_file(file_name, text):
    """writes a test to a given file.
    Args:
        file_name (str): The name of the file to write to.
        test (str): The current of the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)
