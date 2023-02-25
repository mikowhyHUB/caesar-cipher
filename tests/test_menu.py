from unittest.mock import patch
from io import StringIO
from src.menu import Menu


def test_user_menu_choice_main_menu(monkeypatch):
    with patch("builtins.input", side_effect=["1"]):
        menu = Menu(main_menu=True)
        choice = menu.user_menu_choice()
        assert choice == 1


#
# def test_user_menu_choice_additional_options(monkeypatch, capsys):
#     with patch("builtins.input", side_effect=["2"]):
#         menu = Menu(main_menu=False)
#         choice = menu.user_menu_choice()
#         assert choice == 2
#     captured = capsys.readouterr()
#     assert Menu.ADDITIONAL_OPTIONS in captured.out


def test_user_menu_choice_invalid_input(monkeypatch, capsys):
    with patch("builtins.input", side_effect=["a", "b", "1"]):
        menu = Menu(main_menu=True)
        choice = menu.user_menu_choice()
        assert choice == 1
    captured = capsys.readouterr()
    assert "You have entered invalid value. Try again." in captured.out
