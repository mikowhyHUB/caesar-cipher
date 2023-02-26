from typing import Optional, Callable, Dict, Any
from menu import Menu
from cipher import Cipher
from buffer import Text
from file_handler import FileHandler

ROTS = [13, 47]


class Manager:
    """class handling menu operations"""

    def __init__(self):
        self.menu: Menu = Menu()
        self.filehandler: FileHandler = FileHandler()
        self.txt_man: TextManager = TextManager()

        self.menu_options: Dict[int, Callable] = {
            1: self.txt_man.encrypt_text,
            2: self.txt_man.decrypt_text,
            3: self.filehandler.print_file,
            9: exit
        }
        self.submenu_options: Dict[int, Callable] = {
            1: self.txt_man.print_text,
            2: self.txt_man.add_next_text,
            3: self.save_to_json,
            4: self.filehandler.print_file,
            5: self.back_to_menu,
            9: exit
        }

    def run(self) -> None:
        """This code provides a main manu and submenu for the user to select from"""
        print("\nWelcome to Caesar Cipher\n")
        while True:
            try:
                if self.menu.is_main_menu_on:
                    self.menu.user_menu_choice(Menu.MENU_OPTIONS)
                    self.menu_options.get(self.menu.choice)()
                    self.menu.is_main_menu_on = False
                while not self.menu.is_main_menu_on:
                    self.menu.user_menu_choice(Menu.ADDITIONAL_OPTIONS)
                    self.submenu_options.get(self.menu.choice)()
            except TypeError:
                print("Invalid choice. Please try again.")

    def back_to_menu(self):
        self.menu.is_main_menu_on = True

    def save_to_json(self) -> None:
        """Saving JSON file"""
        self.menu.choice = None
        self.back_to_menu()
        self.filehandler.save_file(
            self.txt_man.text.to_dct(self.txt_man.text.status,
                                     self.txt_man.text.rot))


class TextManager:
    """Class handling text operations"""

    def __init__(self) -> None:
        self.text: Text = Text()
        self.cipher: Cipher = Cipher()

    def cipher_that(self, func, status: str)->None
        if self.text.rot is None:
            self.text.buffer.memory.append(func(self.set_rot(), self.set_text()))
            self.text.status = status
        else:
            self.text.buffer.memory.append(func(self.text.rot, self.set_text()))

    def encrypt_text(self) -> None:
        """Encrypting text with ROT 13/47"""
        self.cipher_that(self.cipher.encrypt, 'encrypted')


    def decrypt_text(self) -> None:
        """Decrypting text with ROT 13/47"""
        self.cipher_that(self.cipher.decrypt, 'decrypted')

    def user_choice_rot(self) -> None:
        """User picks what ROT would he like to use"""
        try:
            self.text.rot = int(input("ROT:"))
        except ValueError:
            print(f"Type only {ROTS} numbers")

    def set_rot(self) -> Optional[int]:
        """Setting what ROT user want to use"""
        while self.text.rot not in ROTS:
            print(f"Available rots: {ROTS}")
            self.user_choice_rot()
        return self.text.rot

    def set_text(self) -> str:
        """User typing text to encrypt/decrypt"""
        return input(f"What text would you like to change with ROT{self.text.rot}: ")

    def add_next_text(self) -> None:
        """Adding next decrypted/encrypted text"""
        if self.text.status == "encrypted":
            self.encrypt_text()
        else:
            self.decrypt_text()

    def print_text(self) -> None:
        """Printing users details and encrypted/decrypted text"""
        print(self.text)
