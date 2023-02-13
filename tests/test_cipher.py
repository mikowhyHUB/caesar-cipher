from src.cipher import Cipher
import pytest


@pytest.fixture
def cipher():
    return Cipher()


def test_encrypting_text_with_rot13(cipher):
    assert cipher.encrypt(13, "test") == "grfg"
    assert cipher.encrypt(13, "test test!") == "grfg grfg!"
    assert cipher.encrypt(13, "test2") == "grfg2"


def test_encrypting_text_with_rot47(cipher):
    assert cipher.encrypt(47, "test") == "ozno"
    assert cipher.encrypt(47, "test1") == "ozno1"


def test_decrypting_text_with_rot13(cipher):
    assert cipher.decrypt(13, "grfg") == "test"
    assert cipher.decrypt(13, "grfg3") == "test3"
    assert cipher.decrypt(13, "grfg grfg!") == "test test!"


def test_decrypting_text_with_rot47(cipher):
    assert cipher.decrypt(47, "ozno") == "test"
    assert cipher.decrypt(47, "ozno4") == "test4"
