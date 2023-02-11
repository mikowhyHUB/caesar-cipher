from src.manager import Manager
from src.menu import Menu
import pytest


#
# @pytest.fixture
# def manager():
#     return Manager()


# def test_user_enter_invalid_number():
# manager = Manager()
# expected = manager.menu_options[1]
# actual = 1
# assert manager.menu_choice(actual) == expected
# # assert manager.main_menu() == manager.menu_options


def test_show_menu_method():
    with patch("builtins.input", return_value="1"):
        assert Menu.show_menu() == 1


@patch("builtins.print")
def test_show_menu_method(mocked_print):
    with patch("builtins.input", return_value="1"):
        Menu.show_menu()

        assert mocked_print.mock_calls == [call(Menu.INTRO_TEXT)]
