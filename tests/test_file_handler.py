from src.file_handler import FileHandler
import json
import os
import io
import sys


def test_save_file_successfully():
    cipher_dict = {"test_key": "test_value"}
    FileHandler.save_file(cipher_dict)
    assert os.path.isfile("src-data/cipher.json") == True
    with open("src-data/cipher.json", "r", encoding="utf-8") as cipher:
        data = json.load(cipher)
        assert data == cipher_dict
    os.remove("src-data/cipher.json")


def test_save_file_when_the_input_is_none():
    FileHandler.save_file()
    assert os.path.isfile("src-data/cipher.json")
    with open("src-data/cipher.json", "r", encoding="utf-8") as cipher:
        data = json.load(cipher)
        assert data == {}
    os.remove("src-data/cipher.json")


def test_print_file_success(capsys):
    cipher_dict = {"test_key": "test_value"}
    with open("src-data/cipher.json", "w", encoding="utf-8") as cipher:
        json.dump(cipher_dict, cipher, ensure_ascii=False, indent=4)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    FileHandler.print_file()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == str(cipher_dict)
    os.remove("src-data/cipher.json")


def test_print_file_when_file_not_found():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    FileHandler.print_file()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "There is no file.\nReturning to main menu"
