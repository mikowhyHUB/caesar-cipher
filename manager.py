from menu import Menu
from buffer import buffer1
from exceptions import Exceptions
from typing import Optional, Callable, Dict
from cipher import Cipher
import main
from buffer import Buffer

ROTS = [13, 47]


class Manager:
    """Class handling all choices made by user in menu"""

    def __init__(self) -> None:
        super().__init__()  # dlaczego jak zrobię do metody () to się z automatu wywołuje nawet jak jej nie calluje
        # drugie pytanie: dict z możliwościami wyboru w managerze ograniczał mnie, bo nie mogłem podawać argumentów do metod. jest na to sposób? Czy tak jak zrobiłem w cipher jest ok?
        self.exceptions = Exceptions
        self.menu_options: Dict[int, Callable] = {
            1: self.encrypt_rot13,
            2: self.encrypt_rot47,
            3: self.decrypt_rot13,
            4: self.decrypt_rot47,
            5: self.print_file,
            9: self.exit_program,
        }
        self.additional_options: Dict[int, Callable] = {
            1: self.print_text,
            2: self.save_file,
            3: self.main_menu,
            9: self.exit_program,
        }
        main.Buffer()

    def set_rot(self):
        rot = 0
        while rot not in ROTS:  # zabezpiecznie od złych inputow
            print("Available rots: {ROTS}")
            rot = int(input("Chose ROT 13/47"))
        self.rot = rot
        return self.rot

    def set_text(self):
        self.text = input("What text would you like to change: ")
        return self.text

    def encrypt_text(self):
        cipher = Cipher(self.rot, self.text)
        cipher.encrypt()

    def menu_choice(self, choice: int) -> None:  # sprobowac z  match -> switch keys
        """Choosing option what user made in main menu"""
        self.menu_options.get(choice, self.wrong_number)()

    def additional_choice(self, choice: int) -> None:
        """Choosing option what user made in additional menu"""
        self.additional_options.get(choice, self.wrong_number)()

    def print_text(self) -> None:
        """Printing users encrypted/decrypted text"""
        print(f"\nChanged text: {buffer1.name}\n")
        print("Returning to main menu")

    def exit_program(self) -> None:
        quit()

    def main_menu(self) -> Optional[int]:
        """Showing options user has"""
        choice = self.show_menu()
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
