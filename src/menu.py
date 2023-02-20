class Menu:
    def __init__(self):
        self.main_menu = True

    """Class responsible for printing options to terminal for user"""

    MENU_OPTIONS: str = (
        "Options:\n"
        "1: Encrypt text\n"
        "2: Decrypt text\n"
        "3: Show saved file\n"
        "9: Exit program\n"
    )
    ADDITIONAL_OPTIONS: str = (
        "\nWhat would you like to do with changed text:\n"
        "1: Print\n"
        "2: Add next text\n"
        "3: Save to file\n"
        "4: Show saved file\n"
        "5: Main menu\n"
        "9: Exit program\n"
    )

    # @staticmethod
    # def intro() -> None:
    #     """Printing intro text"""
    #     print(Menu.INTRO_TEXT)

    @staticmethod
    def user_menu_choice() -> int:
        """Printing main menu options"""
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
