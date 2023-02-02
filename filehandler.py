import json
from cipher import Cipher
from buffer import buffer1


class FileHandler(Cipher):
    def __init__(self):
        super().__init__()
        self.json_dict: dict = {}

    def adding_name_to_cipher(self) -> None:
        name_text = input('How would you like to name this text: ')
        self.json_dict[name_text] = buffer1.name

    def changing_to_dict(self):
        self.adding_name_to_cipher()
        self.json_dict['status'] = buffer1.status
        self.json_dict['rot'] = buffer1.rot

    def saving_file(self):
        self.changing_to_dict()
        with open('cipher.json', 'w', encoding='utf-8') as cipher:
            json.dump(self.json_dict, cipher, ensure_ascii=False, indent=4)
            print('File saved. Returning to main menu')

    def printing_file(self):
        with open('cipher.json') as cipher:
            print(json.load(cipher))
