from menu import Menu
from typing import Optional, Callable, Dict, Any
from cipher import Cipher
from buffer import Buffer
from file_handler import FileHandler

ROTS = [13, 47]


class TextManager:
    """Class handling text operations"""

    def __init__(self) -> None:
        self.buffer: Any = Buffer()
        self.cipher: Any = Cipher()

    def encrypt_text(self) -> None:
        """Encrypting text with ROT 13/47"""
        if self.buffer.text.rot is None:
            self.buffer.text.memory.append(self.cipher.encrypt(self.set_rot(), self.set_text()))
            self.buffer.text.status = "encrypted"
            self.set_text_name()
        else:
            self.buffer.text.memory.append(self.cipher.encrypt(self.buffer.text.rot, self.set_text()))

    def decrypt_text(self) -> None:
        """Decrypting text with ROT 13/47"""
        if self.buffer.text.rot is None:
            self.buffer.text.memory.append(self.cipher.decrypt(self.set_rot(), self.set_text()))
            self.buffer.text.status = "decrypted"
            self.set_text_name()
        else:
            self.buffer.text.memory.append(self.cipher.decrypt(self.buffer.text.rot, self.set_text()))

    def user_choice_rot(self) -> None:
        '''User pick what ROT would he like to use'''
        try:
            self.buffer.text.rot = int(input("ROT:"))
        except ValueError:
            print(f"Type only {ROTS} numbers")

    def set_rot(self) -> Optional[int]:
        """Setting what ROT user want to use"""
        while self.buffer.text.rot not in ROTS:
            print(f"Available rots: {ROTS}")
            self.user_choice_rot()
            return self.buffer.text.rot

    def set_text(self) -> str:
        """User typing text to encrypt/decrypt"""
        return input(f"What text would you like to change with ROT{self.buffer.text.rot}: ")

    def set_text_name(self) -> None:
        """Name of list of texts"""
        self.buffer.text.name = input("Name of your text: ")

    def add_next_text(self) -> None:
        """Adding next decrypted/encrypted text"""
        if self.buffer.text.status == "encrypted":
            self.encrypt_text()
        else:
            self.decrypt_text()

    def print_text(self) -> None:
        """Printing users details and encrypted/decrypted text"""
        print(self.buffer.text)
        print("\nReturning to main men\n")


class MenuManager:
    '''class handling menu operations'''

    def __init__(self):
        self.menu = Menu()
        self.filehandler = FileHandler()
        self.txt_man = TextManager()

        self.menu_options: Dict[int, Callable] = {
            1: self.txt_man.encrypt_text,
            2: self.txt_man.decrypt_text,
            3: self.filehandler.print_file,
            9: self.exit_program,
        }
        self.additional_options: Dict[int, Callable] = {
            1: self.txt_man.print_text,
            2: self.txt_man.add_next_text,
            3: self.save_to_json,
            4: self.filehandler.print_file,
            5: self.menu.show_menu,
            9: self.exit_program,
        }

    def save_to_json(self) -> None:
        """Saving JSON file"""
        self.filehandler.save_file(
            self.txt_man.buffer.text.to_dct(
                self.txt_man.buffer.text.name, self.txt_man.buffer.text.memory, self.txt_man.buffer.text.status,
                self.txt_man.buffer.text.rot
            )
        )

    def main_menu(self) -> Optional[int]:
        """Showing options user has and selecting one from menu_options dict"""
        choice = self.menu.show_menu()
        self.menu_options.get(choice, self.wrong_number)()
        return choice

    def additional_menu(self) -> Optional[int]:
        """Showing options what user can do with encrypted/decrypted text"""
        choice = self.menu.show_additional_options()
        self.additional_options.get(choice, self.wrong_number)()
        return choice

    @staticmethod
    def wrong_number() -> None:
        """Handles invalid menu choices"""
        print("Invalid choice. Please try again.")

    @staticmethod
    def exit_program() -> None:
        quit()
