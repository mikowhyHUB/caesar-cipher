import json


class FileHandler:
    """Class operating changed text with JSON"""
    test = {1: 'asd', 2: 'sss'}

    @staticmethod
    def save_file(cipher_dict=None) -> None:
        """Saving to JSON file"""
        if cipher_dict is None:
            cipher_dict = {}
        with open("./cipher.json", "w", encoding="utf-8") as cipher:
            json.dump(cipher_dict, cipher, ensure_ascii=False, indent=4)
            print("File saved. Returning to main menu")

    @staticmethod
    def print_file() -> None:
        """Showing saved file on terminal"""
        try:
            with open("./cipher.json") as cipher:
                print(json.load(cipher))
        except FileNotFoundError:
            print("There is no file.\nReturning to main menu\n")

    # def save_to_json(self) -> None:
    #     """Saving JSON file"""
    #     buffer = Buffer()
    #     buffer.text.to_dct(buffer.text.name, buffer.text.memory, buffer.text.status, buffer.text.rot)
    #     self.save_file(buffer.text.dic)
