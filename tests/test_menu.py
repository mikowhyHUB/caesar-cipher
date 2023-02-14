from src.menu import Menu
from unittest.mock import patch, call
import sys
from io import StringIO
import pytest


def test_is_intro_printing(capfd):
    m = Menu()
    m.intro()
    captured = capfd.readouterr()
    assert captured.out == "\nWelcome to Caesar Cipher\n\n"


def test_show_menu_method():
    with patch("builtins.input", return_value="1"):
        assert Menu.show_menu() == 1


def test_show_menu_invalid(monkeypatch):
    user_input = '7'
    with patch('builtins.input', side_effect=user_input):
        assert Menu.show_menu() == 7


def test_show_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 2)
    i = Menu.show_menu()
    assert i == 2


@patch("builtins.print")
def test_show_menu_methods(mocked_print):
    with patch("builtins.input", return_value="1"):
        Menu.show_menu()

        assert mocked_print.mock_calls == [call(Menu.INTRO_TEXT)]


def test_show_additional_options():
    with patch("builtins.input", return_value="1"):
        assert Menu.show_additional_options() == 1


def test_show_additional_options_invalid(monkeypatch):
    user_input = '7'
    with patch('builtins.input', side_effect=user_input):
        assert Menu.show_additional_options() == 7


@patch("builtins.print")
def test_show_additional_options_methods(mocked_print):
    with patch("builtins.input", return_value="1"):
        Menu.show_additional_options()
