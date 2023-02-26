from src.file_handler import FileHandler
import json
import os
import io
import sys


def test_save_file():
    # Prepare test data
    data = {"key": "value"}
    file_path = "src-data/cipher.json"

    # Test file saved correctly
    FileHandler.save_file(data)
    assert os.path.exists(file_path)

    # Test file contents are correct
    with open(file_path) as f:
        assert json.load(f) == data

    # Clean up
    os.remove(file_path)


def test_print_file_when_file_not_found():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    FileHandler.print_file()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "There is no file.\nReturning to main menu"
