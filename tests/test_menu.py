from unittest.mock import patch
from io import StringIO
from src.menu import Menu


class TestMenu:

    def setup_method(self):
        self.menu = Menu()

    def test_valid_menu_choice(self, monkeypatch):
        input_string = '2\n'
        with patch('sys.stdin', StringIO(input_string)):
            choice = self.menu.user_menu_choice('Enter your choice: ')
        assert choice == 2

    def test_invalid_menu_choice(self, monkeypatch):
        input_string = 'invalid\n2\n'
        with patch('sys.stdin', StringIO(input_string)):
            choice = self.menu.user_menu_choice('Enter your choice: ')
        assert choice == 2

    def test_another_input_choice(self, monkeypatch):
        input_string = '1 2 3\n2\n'
        with patch('sys.stdin', StringIO(input_string)):
            choice = self.menu.user_menu_choice('Enter your choice: ')
        assert choice == 2
