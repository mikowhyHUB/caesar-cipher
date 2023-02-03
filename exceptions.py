class Exceptions:
    def __init__(self):
        pass

    def default_choice(self) -> None:
        """Handles invalid menu choices"""
        print("Invalid choice. Please try again.")

    @staticmethod
    def main_menu_inputs(choice):
        if choice not in [1, 2, 3, 4, 5, 9]:
            print("Invalid choice. Please try again.")
        elif choice == 6:
            raise ValueError("You need to pick an option")

    @staticmethod
    def wrong_number() -> None:
        """Handles invalid menu choices"""
        print("Invalid choice. Please try again.")

    @staticmethod  # nie dziala. nie wychodzi z petli
    def exception_handler(func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except ValueError:
                print("You have entered invalid value. Try again.")
            else:
                return func(*args, **kwargs)
            return inner_function
