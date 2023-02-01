from dataclasses import dataclass
import string
import json


class Cipher:
    def __init__(self):
        self.cipher_text = {'name': 'TO TEST', 'status': '', 'rot': ''}

    def encrypt_rot13(self) -> dict:
        rot13 = 13
        encrypted = ""
        plain_text = input(
            'test encrypt_rot13: ')
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + rot13 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + rot13 - 97) % 26 + 97)
        self.cipher_text['name'], self.cipher_text['status'], self.cipher_text['rot'] = encrypted, 'encrypted', 'ROT13'
        return self.test

    def encrypt_rot47(self) -> None:
        ROT47 = 47
        encrypted = ""
        plain_text = input('test encrypt_rot47: ')
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + ROT47 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + ROT47 - 97) % 26 + 97)
        return self.buffer.encrypted.append(encrypted)

    def decrypt_rot13(self) -> str:
        alphabet = string.ascii_lowercase
        rot13 = 13
        decrypted = ""
        cipher_text = input('test decrypt_rot13: ')
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - rot13) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        self.cipher_text = decrypted
        return self.cipher_text

    def decrypt_rot47(self) -> str:
        alphabet = string.ascii_lowercase
        ROT47 = 47
        decrypted = ""
        cipher_text = input('test decrypt_rot47: ')
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - ROT47) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        return decrypted


class FileHandler(Cipher):
    def __init__(self):
        super().__init__()

    def adding_name_to_cipher(self) -> dict:
        name_text = input('How would you like to name this text: ')
        self.cipher_text[name_text] = self.cipher_text['name']
        del self.cipher_text['name']
        return self.cipher_text

    def saving_file(self):
        json_dict = self.adding_name_to_cipher()
        with open('cipher.json', 'w', encoding='utf-8') as file:
            json.dump(json_dict, file, sort_keys=True, ensure_ascii=False, indent=4)
            print('File saved. Returning to main menu')

    def printing_file(self):
        with open('cipher.json') as file:
            print(json.load(file))


class Buffer(Cipher):
    def __init__(self):
        super().__init__()
        self.menu = Menu()
        self.filefandler = FileHandler()
        self.manager = Manager()
        self.menu_options = {
            1: self.encrypt_rot13,
            2: self.encrypt_rot47,
            3: self.decrypt_rot13,
            4: self.decrypt_rot47,
            5: self.filefandler.printing_file,
            9: exit
        }
        self.additional_options = {
            1: self.print_text,
            2: self.filefandler.saving_file,
            3: self.manager.start,
            9: exit
        }

    def menu_choice(self, choice):
        return self.menu_options.get(choice)()

    def additional_choice(self, choice):
        return self.additional_options.get(choice)()

    def print_text(self):
        print(self.cipher_text['name'])


class Menu:

    def welcome(self):
        print('Welcome to Caesar Cipher\nMain Menu:')

    def show_menu(self):
        return int(input(
            'Options:\n1: Encrypt text with ROT13\n2: Encrypt text with ROT47\n3: Decrypt text with ROT13\n4: Decrypt text with ROT14\n5: Show saved file 9: Exit program '))

    def show_additional_options(self):
        return int(
            input(
                'What would you like to do with changed text:\n1: Print\n2: Save to file\n4: Main menu\n5: Exit program'))


class Manager:

    def __init__(self):
        self.buffer = Buffer()
        self.menu = Menu()

    def start(self) -> int:
        self.menu.welcome()
        choice = self.menu.show_menu()
        self.buffer.menu_choice(choice)
        return choice

    def options_encrypted(self) -> int:
        choice = self.menu.show_additional_options()
        self.buffer.additional_choice(choice)
        return choice


def main():
    manager = Manager()

    # x = manager.start()  # while true petla z opcjami
    # if x == 1:
    #     manager.options_encrypted()
    # elif x == 3:
    #     manager.options_encrypted()

    # manager.options_encrypted()


if __name__ == '__main__':
    main()

'''Pytania:
1. dlaczego w menu_options jak zrobię do metody () to się z automatu wywołuje nawet jak jej nie calluje
2. Po co dziedziczyć skoro można w __init__ zrobić atrybut jako dana klasa i mamy te same metody dostępne
3. Czy tam gdzie pycharm mi podkresla by powinno byc staticmethod to robic staticmethod?
3. Jaki jest proces twórczy osoby doświadczonej. Co po kolei robi'''
