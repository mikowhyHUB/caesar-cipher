from dataclasses import dataclass
import string


class Cipher:
    def __init__(self):
        self.cipher_text = ''
        self.decrypted_text = ''

    def encrypt_rot13(self) -> str:
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
        self.cipher_text = encrypted
        return self.cipher_text  # a jakby tak zrobic string zamiast list i za kazdym razem jak chce user w menu dodasc nastepny yo sie zamienia. bo jak appendujesz do listy to gorzej

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


class FileHandler:
    pass


class Buffer(Cipher):
    def __init__(self):
        super().__init__()
        self.menu = Menu()
        self.menu_options = {1: self.encrypt_rot13, 3: self.decrypt_rot13}
        self.additional_options = {1: self.print_text, 2: 'save to file'}

    def menu_choice(self, choice):
        return self.menu_options.get(choice)()

    def additional_choice(self, choice):
        return self.additional_options.get(choice)()

    def print_text(self):
        print(self.cipher_text)


class Menu:

    def welcome(self):
        print('Welcome to Caesar Cipher')

    def show_menu(self):
        return int(input('Options 1: encrypt13, 2: encrypt47, 3: decrpt13, 4: decrypt14, 5: show files, 6: exit '))

    def show_additional_options(self):
        return int(
            input(
                'What would you like to do with changed text: 1print, 2add another, 3save to file, 4 main menu, 4.quit...'))

    # def show_decrypt_options(self):
    #     return int(
    #         input('What would you like to do with decrypted text: 1print, 2add another, 3save to file, 4 main menu, 4.quit...'))


class Manager:

    def __init__(self):
        self.buffer = Buffer()
        self.menu = Menu()

    def start(self):
        self.menu.welcome()
        choice = self.menu.show_menu()
        self.buffer.menu_choice(choice)
        return choice

    def options_encrypted(self):
        choice = self.menu.show_additional_options()
        self.buffer.additional_choice(choice)
        return choice


def main():
    manager = Manager()
    menu = Menu()

    x = manager.start()  # while true petla z opcjami
    if x == 1:
        manager.options_encrypted()
    elif x == 3:
        manager.options_encrypted()
    # manager.options_encrypted()


if __name__ == '__main__':
    main()

'''Pytania:
1. dlaczego w menu_options jak zrobię do metody () to się z automatu wywołuje nawet jak jej nie calluje
2. Po co dziedziczyć skoro można w __init__ zrobić atrybut jako dana klasa i mamy te same metody dostępne 
3. Jaki jest proces twórczy osoby doświadczonej. Co po kolei robi'''
