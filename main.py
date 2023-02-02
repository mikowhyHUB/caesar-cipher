import string
import json


class Cipher:
    # nie aktualizuje sie dict
    def __init__(self) -> None:
        self.ROT13 = 13
        self.ROT47 = 47
        self.cipher_text = {'name': '', 'status': '', 'rot': ''}  # spróbować dzialac na ROT13 i drugi na ROT47

    def encrypt_rot13(self) -> dict:
        encrypted = ""
        plain_text = input('What text would you like to encrypt: ')
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + self.ROT13 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + self.ROT13 - 97) % 26 + 97)
        self.cipher_text['name'], self.cipher_text['status'], self.cipher_text['rot'] = encrypted, 'encrypted', 'ROT13'
        return self.cipher_text

    def encrypt_rot47(self) -> dict:
        encrypted = ""
        plain_text = input('What text would you like to encrypt: ')
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + self.ROT47 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + self.ROT47 - 97) % 26 + 97)
        self.cipher_text['name'], self.cipher_text['status'], self.cipher_text['rot'] = encrypted, 'encrypted', 'ROT47'
        return self.cipher_text

    def decrypt_rot13(self) -> dict:
        alphabet = string.ascii_lowercase
        decrypted = ""
        cipher_text = input('What text would you like to decrypt: ')
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - self.ROT13) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        self.cipher_text['name'], self.cipher_text['status'], self.cipher_text['rot'] = decrypted, 'decrypted', 'ROT13'
        return self.cipher_text

    def decrypt_rot47(self) -> dict:
        alphabet = string.ascii_lowercase
        decrypted = ""
        cipher_text = input('What text would you like to decrypt: ')
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - self.ROT47) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        self.cipher_text['name'], self.cipher_text['status'], self.cipher_text['rot'] = decrypted, 'decrypted', 'ROT47'
        return self.cipher_text


class FileHandler(Cipher):

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


class Buffer(FileHandler):
    def __init__(self):
        super().__init__()
        # self.manager = Manager()

        self.menu_options = {
            1: self.encrypt_rot13,
            2: self.encrypt_rot47,
            3: self.decrypt_rot13,
            4: self.decrypt_rot47,
            5: self.printing_file,
            9: self.exit_program
        }
        self.additional_options = {
            1: self.print_text,
            2: self.saving_file,
            # 3: Manager.main_menu,
            9: self.exit_program
        }

    def menu_choice(self, choice):
        return self.menu_options.get(choice)()

    def additional_choice(self, choice):
        return self.additional_options.get(choice)()

    def print_text(self):
        print(self.cipher_text['name'])

    def exit_program(self):  # to do managera
        quit()


class Menu(Buffer):

    def welcome(self):
        print('Welcome to Caesar Cipher\nMain Menu:')

    def show_menu(self):  # 6: decrypt from file
        return int(input(
            'Options:\n1: Encrypt text with ROT13\n2: Encrypt text with ROT47\n3: Decrypt text with ROT13\n4: Decrypt text with ROT14\n5: Show saved file\n9: Exit program\n'))

    def show_additional_options(self):
        return int(
            input(
                'What would you like to do with changed text:\n1: Print\n2: Save to file\n4: Main menu\n9: Exit program\n'))


class Manager(Menu):

    def __init__(self):
        super().__init__()

    def main_menu(self) -> int:
        self.welcome()
        choice = self.show_menu()
        self.menu_choice(choice)
        return choice

    def additional_menu(self) -> int:
        choice = self.show_additional_options()
        self.additional_choice(choice)
        return choice


def main():
    manager = Manager()
    while True:
        start = manager.main_menu()
        if start in [1, 2, 3, 4]:
            manager.additional_menu()


if __name__ == '__main__':
    main()

'''Pytania:
1. dlaczego w menu_options jak zrobię do metody () to się z automatu wywołuje nawet jak jej nie calluje
2. Po co dziedziczyć skoro można w __init__ zrobić atrybut jako dana klasa i mamy te same metody dostępne
3. Czy tam gdzie pycharm mi podkresla by powinno byc staticmethod to robic staticmethod?
4. odnośnie branchy. Jak zmerdżuje z mainem to usuwać branch?
3. Jaki jest proces twórczy osoby doświadczonej. Co po kolei robi'''
