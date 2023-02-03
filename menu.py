from filehandler import FileHandler


class Menu(FileHandler):
    """Class printing options to terminal for user"""

    def intro(self) -> None:
        print("\nWelcome to Caesar Cipher\n")

    def show_menu(self) -> int:
        self.intro()  # 6: decrypt from file
        return int(
            input(
                "Options:\n1: Encrypt text with ROT13\n2: Encrypt text with ROT47\n3: Decrypt text with ROT13\n"
                "4: Decrypt text with ROT14\n5: Show saved file\n9: Exit program\n"
            )
        )

    def show_additional_options(self) -> int:
        return int(
            input(
                "What would you like to do with changed text:\n1: Print\n"
                "2: Save to file\n4: Main menu\n9: Exit program\n"
            )
        )
