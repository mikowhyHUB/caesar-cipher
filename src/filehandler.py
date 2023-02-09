import json


class FileHandler:
    """Class operating changed text with JSON"""

    @staticmethod
    def save_file(cipher_dict: dict) -> None:
        """Saving to JSON file"""
        with open("../cipher.json", "w", encoding="utf-8") as cipher:
            json.dump(cipher_dict, cipher, ensure_ascii=False, indent=4)
            print("File saved. Returning to main menu")

    @staticmethod
    def print_file() -> None:
        """Showing saved file on terminal"""
        try:
            with open("../cipher.json") as cipher:
                print(json.load(cipher))
        except FileNotFoundError:
            print("There is no file.\nReturning to main menu\n")
