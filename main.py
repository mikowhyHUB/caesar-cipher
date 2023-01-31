from dataclasses import dataclass
import string


class Cipher:
    def __init__(self):
        self.test_encrypted = []

    def encrypt(self) -> None:
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
        return self.test_encrypted.append(encrypted)

    def decrypt(self, cipher_text: str) -> str:
        alphabet = string.ascii_lowercase
        n = 13
        decrypted = ""
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - n) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        return decrypted

    def printing(self):
        print(self.test_encrypted)


class FileHandler:
    pass


class Buffer:
    def __init__(self):
        self.cipher = Cipher()
        self.menu = Menu()
        self.menu_options = {1: self.cipher.encrypt, 2: self.cipher.decrypt}
        self.file_options = {1: self.cipher.test_encrypted, 2: 'save to file'}

    def menu_choice(self, x):
        return self.menu_options.get(x)()

    def file_option(self):
        print(self.file_options.get(self.menu.show_file_options()))


class Menu:

    def welcome(self):
        print('Welcome to Caesar Cipher')

    def show_menu(self):
        return int(input('Options 1,2,3: '))

    def show_file_options(self):
        return int(input('What would you like to do with encrypted text: 1print, 2, 3...'))


class Manager:

    def __init__(self):
        self.buffer = Buffer()
        self.menu = Menu()

    def start(self):
        self.menu.welcome()
        x = self.menu.show_menu()
        self.buffer.menu_choice(x)
        return x

    def options(self):
        self.buffer.file_option()


def main():
    manager = Manager()
    menu = Menu()

    x = manager.start()
    if x == 1:
        manager.options()


if __name__ == '__main__':
    main()

'''Pytania:
1. dlaczego w menu_options jak zrobię do metody () to się z automatu wywołuje nawet jak jej nie calluje
2. Po co dziedziczyć skoro można w __init__ zrobić atrybut jako dana klasa i mamy te same metody dostępne 
3. Jaki jest proces twórczy osoby doświadczonej. Co po kolei robi'''
