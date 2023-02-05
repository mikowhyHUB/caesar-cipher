from time import sleep
from manager import Manager


def main():
    manager = Manager()
    manager.test()
    # while True:
    #     start = manager.main_menu()
    #     if start in [1, 2]:
    #         sleep(1)
    #         additional = manager.additional_menu()
    #         sleep(1)
    #         while additional == 2:
    #             manager.additional_menu()


if __name__ == "__main__":
    main()
