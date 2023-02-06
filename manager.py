from menu import Menu
from typing import Optional, Callable, Dict, Any
from cipher import Cipher
from buffer import Buffer, Text

from filehandler import FileHandler

ROTS = [13, 47]


class Manager:
    """Class handling all choices made by user in menu"""

    def __init__(self) -> None:
        self.menu: Any = Menu()
        self.buffer: Any = Buffer()
        self.filehandler: Any = FileHandler()
        self.text: Any = Text()
        self.cipher_dict = {}

        self.menu_options: Dict[int, Callable] = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.filehandler.print_file,
            9: self.exit_program,
        }
        self.additional_options: Dict[int, Callable] = {
            1: self.print_text,
            2: self.add_next_text,
            3: self.save_to_json,
            4: self.filehandler.print_file,
            5: self.menu.show_menu,
            9: self.exit_program,
        }

    def set_rot(self):
        rot = 0
        while rot not in ROTS:
            print(f"Available rots: {ROTS}")
            rot = int(input())  # zabezpieczyc przed valueerr
        self.text.rot = rot
        return rot

    def save_to_json(self):
        self.filehandler.save_file(
            self.text.to_dct(
                self.text.name, self.buffer.memory, self.text.status, self.text.rot
            )
        )

    def set_text(self):
        return input(f"What text would you like to change with ROT{self.text.rot}: ")

    def set_text_name(self):
        self.text.name = input("Name of your text: ")

    def print_text(self) -> None:
        """Printing users encrypted/decrypted text"""
        self.cipher_dict = self.text.to_dct(
            self.text.name, self.buffer.memory, self.text.status, self.text.rot
        )
        for key, value in self.cipher_dict.items():
            print(f"{key} : {value}")
        print("\nReturning to main men\n")

    def encrypt_text(self):
        if self.text.rot is None:
            cipher = Cipher(self.set_rot(), self.set_text())
            self.buffer.memory.append(cipher.encrypt(cipher.rot, cipher.text))
            self.text.status = "encrypted"
            self.set_text_name()
        else:
            cipher = Cipher(self.text.rot, self.set_text())
            self.buffer.memory.append(cipher.encrypt(cipher.rot, cipher.text))

    def decrypt_text(self):
        if self.text.rot is None:
            cipher = Cipher(self.set_rot(), self.set_text())
            self.buffer.memory.append(cipher.decrypt(cipher.rot, cipher.text))
            self.text.status = "decrypted"
            self.set_text_name()
        else:
            cipher = Cipher(self.text.rot, self.set_text())
            self.buffer.memory.append(cipher.decrypt(cipher.rot, cipher.text))

    def add_next_text(self):
        if self.text.status is "encrypted":
            self.encrypt_text()
        else:
            self.decrypt_text()

    def menu_choice(self, choice: int) -> None:  # sprobowac z  match -> switch keys
        """Choosing option what user made in main menu"""
        self.menu_options.get(choice, self.wrong_number)()

    def additional_choice(self, choice: int) -> None:
        """Choosing option what user made in additional menu"""
        self.additional_options.get(choice, self.wrong_number)()

    def main_menu(self) -> Optional[int]:
        """Showing options user has"""
        choice = self.menu.show_menu()
        self.menu_choice(choice)
        return choice

    def additional_menu(self) -> Optional[int]:
        """Showing options what user can do with encrypted/decrypted text"""
        choice = self.menu.show_additional_options()
        self.additional_choice(choice)
        return choice

    def wrong_number(self) -> None:
        """Handles invalid menu choices"""
        print("Invalid choice. Please try again.")

    def exit_program(self) -> None:
        quit()
