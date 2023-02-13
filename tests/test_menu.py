from src.menu import Menu
from unittest.mock import patch, call
import sys
from io import StringIO
import pytest


# def test_is_intro_printing():
#     outcome = "\nWelcome to Caesar Cipher\n"
#     assert Menu.intro() == outcome


def test_show_menu_method():
    with patch("builtins.input", return_value="1"):
        assert Menu.show_menu() == 1


# def test_show_menu_value_error(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: 2)
#     with pytest.raises(ValueError) as exc_info:
#         m = Menu()
#         m.xyz()
#     exception_raised = exc_info.value


def test_show_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 2)
    i = Menu.show_menu()
    assert i == 2


@patch("builtins.print")
def test_show_menu_methods(mocked_print):
    with patch("builtins.input", return_value="1"):
        Menu.show_menu()

        assert mocked_print.mock_calls == [call(Menu.INTRO_TEXT)]
