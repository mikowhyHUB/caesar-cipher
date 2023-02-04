import json
from cipher import Cipher


# from buffer import buffer1


class FileHandler:
    """Class operating on Buffer object"""

    # TO DO możliwe, że fileHandler będzie mógł nie posiadać obiektu.
    def __init__(self) -> None:
        self._json_dict: dict = {}

    def name_the_cipher(self) -> None:
        """User can choose how his text should be named in JSON file"""
        name_text = input("How would you like to name this text: ")
        self._json_dict[name_text] = buffer1.name

    def prepare_dict(self) -> None:
        """Preparing Buffer object to dict"""
        self.name_the_cipher()
        self._json_dict["status"] = buffer1.status
        self._json_dict["rot"] = buffer1.rot

    def save_file(
        self,
    ) -> None:  # data) -> None:
        """Saving to JSON file"""
        self.prepare_dict()
        with open("cipher.json", "w", encoding="utf-8") as cipher:
            json.dump(self._json_dict, cipher, ensure_ascii=False, indent=4)
            print("File saved. Returning to main menu")

    def print_file(self) -> None:
        """Showing saved file on terminal"""
        with open("cipher.json") as cipher:
            print(json.load(cipher))
