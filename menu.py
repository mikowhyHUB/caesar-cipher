class Menu:
    """Class responsible for printing options to terminal for user"""

    def __init__(self) -> None:
        super().__init__()
        self._intro_text = "\nWelcome to Caesar Cipher\n"
        self._menu_options: str = (
            "Options:\n"
            "1: Encrypt text with ROT13\n"
            "2: Encrypt text with ROT47\n"
            "3: Decrypt text with ROT13\n"
            "4: Decrypt text with ROT47\n"
            "5: Show saved file\n"
            "9: Exit program\n"
        )
        self._additional_options = (
            "What would you like to do with changed text:\n"
            "1: Print\n"
            "2: Save to file\n"
            "3: Main menu\n"
            "9: Exit program\n"
        )

    def intro(self) -> None:
        """Printing intro text"""
        print(self._intro_text)

    def show_menu(self) -> int:
        """Printing main menu options"""
        self.intro()
        while True:
            try:
                return int(input(self._menu_options))
            except ValueError:
                print("You have entered invalid value. Try again.")

    def show_additional_options(self) -> int:
        """Printing additional menu options"""
        while True:
            try:
                return int(input(self._additional_options))
            except ValueError:
                print("You have entered invalid value. Try again.")
