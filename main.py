from dataclasses import dataclass
import string


class Cipher:
    def __init__(self):
        self.test_encrypted = []

    def encrypt_rot13(self) -> None:
        ROT13 = 13
        encrypted = ""
        plain_text = input(
            'test encrypt_rot13: ')  # mozliwe, ze bd musial to zmienic i dodawac w self bo koliduje z zapisywaniem plikow
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + ROT13 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + ROT13 - 97) % 26 + 97)
        return self.test_encrypted.append(encrypted)

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
        return self.test_encrypted.append(encrypted)

    def decrypt_rot13(self) -> str:
        alphabet = string.ascii_lowercase
        ROT13 = 13
        decrypted = ""
        cipher_text = input('test decrypt_rot13: ')
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - ROT13) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        return decrypted

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


class FileHandler:
    pass


class Buffer:
    def __init__(self):
        self.cipher = Cipher()
        self.menu = Menu()
        self.menu_dict = {1: self.cipher.encrypt_rot13, 2: self.cipher.decrypt_rot13}
        self.encrypt_dict = {1: self.cipher.test_encrypted, 2: 'save to file'}

    def menu_choice(self, x):
        return self.menu_dict.get(x)()

    def encrypt_options(self):
        print(self.encrypt_dict.get(self.menu.show_encrypt_options()))


class Menu:

    def welcome(self):
        print('Welcome to Caesar Cipher')

    def show_menu(self):
        return int(input('Options 1: encrypt13, 2: encrypt47, 3: decrpt13, 4: decrypt14, 5: show files, 6: exit '))

    def show_encrypt_options(self):
        return int(
            input('What would you like to do with encrypted text: 1print, 2add another, 3save to file, 4.quit...'))

    def show_decrypt_options(self):
        return int(
            input('What would you like to do with decrypted text: 1print, 2add another, 3save to file, 4.quit...'))


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
        self.buffer.encrypt_options()


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
