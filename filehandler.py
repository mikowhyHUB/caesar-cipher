import json
from cipher import Cipher
from buffer import buffer1


class FileHandler(Cipher):
    """Class operating on Buffer object"""

    def __init__(self) -> None:
        super().__init__()
        self.json_dict: dict = {}

    def add_name_to_cipher(self) -> None:
        """User can choose how his text should be named in JSON file"""
        name_text = input("How would you like to name this text: ")
        self.json_dict[name_text] = buffer1.name

    def change_to_dict(self) -> None:
        """Preparing Buffer object to dict"""
        self.add_name_to_cipher()
        self.json_dict["status"] = buffer1.status
        self.json_dict["rot"] = buffer1.rot

    def save_file(self) -> None:
        """Saving to JSON file"""
        self.change_to_dict()
        with open("cipher.json", "w", encoding="utf-8") as cipher:
            json.dump(self.json_dict, cipher, ensure_ascii=False, indent=4)
            print("File saved. Returning to main menu")

    def print_file(self) -> None:
        """Showing saved file on terminal"""
        with open("cipher.json") as cipher:
            print(json.load(cipher))
