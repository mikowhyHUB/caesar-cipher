from dataclasses import dataclass
import string


class Cipher:

    def encrypt(self) -> str:
        ROT13 = 13
        encrypted = ""
        plain_text = input('test encrypt: ')
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + ROT13 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + ROT13 - 97) % 26 + 97)
        return encrypted

    def decrypt(self, cipher_text: str) -> str:
        alphabet = string.ascii_lowercase
        n = 13
        decrypted_message = ""
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - n) % 26
                new_char = alphabet[new_pos]
                decrypted_message += new_char
            else:
                decrypted_message += char
        return decrypted_message


class FileHandler:
    pass


class Buffer:
    def __init__(self):
        self.cipher = Cipher()
        self.menu = Menu()
        self.menu_options = {1: self.cipher.encrypt, 2: 'test'}
        self.file_options = {1: '...', 2: '...'}

    def execute_choice(self):
        print(self.menu_options.get(self.menu.show_menu())())


class Menu:

    def show_menu(self):
        return int(input('Options 1,2,3: '))

    def show_file_options(self):
        return int('What would you like to do with encrypted text: 1, 2, 3...')


class Manager(Buffer):

    def start(self):
        Buffer().execute_choice()


def main():
    manager = Manager()
    manager.start()


if __name__ == '__main__':
    main()

'''Pytania:
1. dlaczego w menu_options jak zrobię do metody () to się z automatu wywołuje nawet jak jej nie calluje
2. Po co dziedziczyć skoro można w __init__ zrobić atrybut jako dana klasa i mamy te same metody dostępne '''
