from menu import Menu
from buffer import buffer1


class Manager(Menu):

    def __init__(self):
        super().__init__()
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
            3: self.main_menu,
            9: self.exit_program
        }

    def menu_choice(self, choice):
        return self.menu_options.get(choice)()

    def additional_choice(self, choice):
        return self.additional_options.get(choice)()

    def print_text(self):
        print(f'\nChanged text: {buffer1.name}\n')
        print('Returning to main menu')

    def exit_program(self):
        quit()

    def main_menu(self) -> int:
        self.welcome()
        choice = self.show_menu()
        self.menu_choice(choice)
        return choice

    def additional_menu(self) -> int:
        choice = self.show_additional_options()
        self.additional_choice(choice)
        return choice
