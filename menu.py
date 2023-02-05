class Menu:
    """Class responsible for printing options to terminal for user"""

    INTRO_TEXT: str = "\nWelcome to Caesar Cipher\n"
    MENU_OPTIONS: str = (
        "Options:\n"
        "1: Encrypt text\n"
        "2: Decrypt text\n"
        "3: Show saved file\n"
        "9: Exit program\n"
    )
    ADDITIONAL_OPTIONS: str = (
        "What would you like to do with changed text:\n"
        "1: Print\n"
        "2: Add next text"
        "3: Save to file\n"
        "4: Main menu\n"
        "9: Exit program\n"
    )

    @staticmethod
    def intro() -> None:
        """Printing intro text"""
        print(Menu.INTRO_TEXT)

    @staticmethod
    def show_menu() -> int:
        """Printing main menu options"""
        Menu.intro()
        while True:
            try:
                return int(input(Menu.MENU_OPTIONS))
            except ValueError:
                print("You have entered invalid value. Try again.")

    @staticmethod
    def show_additional_options() -> int:
        """Printing additional menu options"""
        while True:
            try:
                return int(input(Menu.ADDITIONAL_OPTIONS))
            except ValueError:
                print("You have entered invalid value. Try again.")
