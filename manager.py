from menu import Menu
from typing import Optional, Callable, Dict
from cipher import Cipher
from buffer import Buffer, Text
from filehandler import FileHandler

ROTS = [13, 47]


class Manager:
    """Class handling all choices made by user in menu"""

    def __init__(self) -> None:
        self.menu = Menu()
        self.buffer = Buffer()
        self.filehandler = FileHandler()
        self.text = Text()
        self.rot = 0  # pomysl by to zamioenic na obiekt TeXtName. tak samo status
        self.status = ""

        self.menu_options: Dict[int, Callable] = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.print_text,
            9: self.exit_program,
        }
        self.additional_options: Dict[int, Callable] = {
            1: self.print_text,
            2: self.add_next_text,
            3: self.filehandler.save_file,
            4: self.main_menu,
            9: self.exit_program,
        }

    def set_rot(self):
        rot = 0
        while rot not in ROTS:
            print(f"Available rots: {ROTS}")
            rot = int(input())  # zabezpieczyc przed valueerr
        self.rot = rot
        return rot

    def set_text(self):
        text = input(f"What text would you like to change with ROT{self.rot}: ")
        return text

    @staticmethod
    def set_name():
        return input("Name of your text: ")

    def set_text_class(self):
        self.text = Text(self.set_name(), self.status, self.rot)

    def print_text(self) -> None:
        """Printing users encrypted/decrypted text"""
        dct = self.text.to_dct(
            self.text.name, self.buffer.memory, self.text.status, self.text.rot
        )
        print(f"\nChanged text: {dct}\n")
        print("Returning to main menu")

    def encrypt_text(self):
        if self.rot == 0:
            cipher = Cipher(self.set_rot(), self.set_text())
            self.buffer.memory.append(cipher.encrypt(cipher.rot, cipher.text))
            self.status = "encrypted"
            self.set_text_class()
        else:
            cipher = Cipher(self.rot, self.set_text())
            self.buffer.memory.append(cipher.encrypt(cipher.rot, cipher.text))

    def decrypt_text(self):
        cipher = Cipher(self.set_rot(), self.set_text())
        self.buffer.memory.append(cipher.decrypt(cipher.rot, cipher.text))
        self.set_text_class()

    def add_next_text(self):
        if self.status == "encrypted":
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
