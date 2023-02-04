from menu import Menu
from exceptions import Exceptions
from typing import Optional, Callable, Dict
from cipher import Cipher
import main
from buffer import Buffer, Test

ROTS = [13, 47]


class Manager:
    """Class handling all choices made by user in menu"""

    def __init__(self) -> None:
        self.menu = Menu()
        self.buffer = Buffer()
        self.test = self.set_test()
        self.rot = self.set_rot()
        self.text = self.set_text()
        self.name = self.set_name()

        self.menu_options: Dict[int, Callable] = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.print_text,
            9: self.exit_program,
        }
        self.additional_options: Dict[int, Callable] = {
            1: self.print_text,
            2: self.add_next_text,
            3: self.save_file,
            4: self.main_menu,
            9: self.exit_program,
        }
        main.Buffer()

    def set_rot(self):
        rot = 0
        while rot not in ROTS:  # zabezpiecznie od złych inputow
            print("Available rots: {ROTS}")
            rot = int(input())
        self.rot = rot
        return self.rot

    def set_text(self):
        self.text = input("What text would you like to change: ")
        return self.text

    def set_name(self):
        self.name = input("name it bitch: ")
        return self.name

    def set_test(self):
        xyz = Test(self.name, "DO WYKOMBINOWANIA", self.rot)
        return xyz

    def encrypt_text(self):
        cipher = Cipher(self.rot, self.text)
        # cipher.encrypt(cipher.rot, cipher.text)
        self.buffer.memory.append(cipher.encrypt(cipher.rot, cipher.text))
        self.text

    def decrypt_text(self):
        cipher = Cipher(self.rot, self.text)
        # cipher.decrypt(cipher.rot, cipher.text)
        self.buffer.memory.append(cipher.decrypt(cipher.rot, cipher.text))

    def add_next_text(self):
        pass

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

    def print_text(self) -> None:
        """Printing users encrypted/decrypted text"""
        print(f"\nChanged text: {'DO WLOZENIA'}\n")
        print("Returning to main menu")

    def wrong_number(self) -> None:
        """Handles invalid menu choices"""
        print("Invalid choice. Please try again.")

    def exit_program(self) -> None:
        quit()
