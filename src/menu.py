class Menu:
    """Class responsible for printing options to terminal for user"""

    def __init__(self, choice: int = None, is_main_menu_on: bool = True) -> None:
        self.choice = choice
        self.is_main_menu_on = is_main_menu_on

    MENU_OPTIONS: str = (
        "Main Menu:\n"
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
        "5: Back to main menu\n"
        "9: Exit program\n"
    )

    def user_menu_choice(self, prompt: str) -> int:
        """Printing main menu/additional options"""
        while True:
            try:
                self.choice = int(input(prompt))
                return self.choice
            except ValueError:
                print("You have entered invalid value. Try again.")
