from src.cipher import Cipher
import pytest


@pytest.fixture
def cipher():
    return Cipher(13, "test text")


def test_encrypting_text(cipher):
    assert cipher.encrypt(13, "test") == "grfg"
    assert cipher.encrypt(47, "test") == "ozno"


def test_decrypting_text(cipher):
    assert cipher.decrypt(13, "grfg") == "test"
    assert cipher.decrypt(47, "ozno") == "test"
