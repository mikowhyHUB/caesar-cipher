import pytest
from unittest.mock import patch
from src.manager import TextManager


@pytest.fixture
def manager():
    return TextManager()


def test_user_choice_rot_valid_input(manager):
    with patch("builtins.input", return_value="13"):
        manager.user_choice_rot()
        assert manager.buffer.text.rot == 13


def test_user_choice_rot_invalid_input(manager):
    with patch('builtins.input', return_value='invalid'):
        with patch('builtins.print') as mock_print:
            manager.user_choice_rot()
            mock_print.assert_called_with(f"Type only [13, 47] numbers")
        assert manager.buffer.text.rot is None


# def test_set_rot_with_valid_rot(manager):
#     manager.buffer.text.rot = 47
#     assert manager.set_rot() == 47

# def test_set_rot_with_invalid_rot_then_valid_rot(manager):
#     with patch('builtins.input', side_effect=['14', '3']):
#         with patch('builtins.print') as mock_print:
#             assert manager.set_rot() == 14
#             mock_print.assert_called_with(f"Available rots: ")

def test_set_text(manager):
    with patch("builtins.input", return_value="test text"):
        assert manager.set_text() == 'test text'


def test_set_text_name(manager):
    with patch("builtins.input", return_value="test text name"):
        manager.set_text_name()
        assert manager.buffer.text.name == 'test text name'


def test_add_next_text_when_status_is_encrypted(manager):
    manager.buffer.text.status = "encrypted"
    with patch.object(manager, 'encrypt_text') as mock_encrypt:
        manager.add_next_text()
        mock_encrypt.assert_called_once()


def test_add_next_text_when_status_is_decrypted(manager):
    manager.buffer.text.status = "decrypted"
    with patch.object(manager, 'decrypt_text') as mock_decrypt:
        manager.add_next_text()
        mock_decrypt.assert_called_once()
