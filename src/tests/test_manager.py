from src.manager import Manager
from src.menu import Menu
import pytest


#
# @pytest.fixture
# def manager():
#     return Manager()


def test_user_enter_invalid_number():
    manager = Manager()
    expected = manager.menu_options[1]
    actual = 1
    assert manager.menu_choice(actual) == expected
    # assert manager.main_menu() == manager.menu_options
