from typing import Optional, Callable, Dict, Any
from menu import Menu
from cipher import Cipher
from buffer import Text
from file_handler import FileHandler

ROTS = [13, 47]


class MenuManager:
    """class handling menu operations"""

    def __init__(self):
        self.menu = Menu()
        self.filehandler = FileHandler()
        self.txt_man = TextManager()

        self.menu_options: Dict[int, Callable] = {
            1: self.txt_man.encrypt_text,
            2: self.txt_man.decrypt_text,
            3: self.filehandler.print_file,
            9: exit
        }
        self.additional_options: Dict[int, Callable] = {
            1: self.txt_man.print_text,
            2: self.txt_man.add_next_text,
            3: self.save_to_json,
            4: self.filehandler.print_file,
            9: exit
        }

    def start(self):
        while True:
            self.main_menu()
            if self.menu.choice in [1, 2]:
                self.additional_menu()
            while self.menu.choice == 2:
                self.additional_menu()

    def main_menu(self) -> Optional[int]:
        """Showing options user has and selecting one from menu_options dict"""
        try:
            self.menu.user_menu_choice()
            self.menu_options.get(self.menu.choice)()
        except TypeError:
            print("Invalid choice. Please try again.")

    def additional_menu(self) -> Optional[int]:
        """Showing options what user can do with encrypted/decrypted text"""
        choice = self.menu.user_menu_choice()
        self.additional_options.get(self.menu.choice)()
        return choice

    def save_to_json(self) -> None:
        """Saving JSON file"""
        self.menu.choice = None
        self.filehandler.save_file(
            self.txt_man.text.to_dct(self.txt_man.text.status,
                                     self.txt_man.text.rot))


class TextManager:
    """Class handling text operations"""

    def __init__(self) -> None:
        self.text: Any = Text()
        self.cipher: Any = Cipher()

    def encrypt_text(self) -> None:
        """Encrypting text with ROT 13/47"""
        if self.text.rot is None:
            self.text.buffer.memory.append(self.cipher.encrypt(self.set_rot(), self.set_text()))
            self.text.status = "encrypted"
        else:
            self.text.buffer.memory.append(self.cipher.encrypt(self.text.rot, self.set_text()))

    def decrypt_text(self) -> None:
        """Decrypting text with ROT 13/47"""
        if self.text.rot is None:
            self.text.buffer.memory.append(self.cipher.decrypt(self.set_rot(), self.set_text()))
            self.text.status = "decrypted"
        else:
            self.text.buffer.memory.append(self.cipher.decrypt(self.text.rot, self.set_text()))

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
