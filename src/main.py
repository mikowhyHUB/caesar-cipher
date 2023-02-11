from manager import MenuManager


def main():
    manager = MenuManager()
    while True:
        start = manager.main_menu()
        if start in [1, 2]:
            additional = manager.additional_menu()
            while additional == 2:
                manager.additional_menu()


if __name__ == "__main__":
    main()
