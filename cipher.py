import re
from buffer import Buffer
from typing import Pattern
import string
from abc import ABC, abstractmethod


class Cipher:
    """Class for cipher users text"""

    def __init__(self, rot: int, text: str) -> None:
        self.rot = rot
        self.text = text

    def encrypt(self, plain_text) -> None:
        """Encrypting users text with ROT13 or ROT47 method"""
        encrypted: str = ""
        for char in plain_text:
            if char == " ":
                encrypted += " "
            elif (
                char.isalpha()
            ):  # char in [string.ascii_lowercase, string.ascii_uppercase]:
                if char.isupper():
                    encrypted += chr((ord(char) + self.rot - 65) % 26 + 65)
                else:
                    encrypted += chr((ord(char) + self.rot - 97) % 26 + 97)
            else:
                encrypted += char

    def decrypt(self, cipher_text) -> None:
        """Decrypting users text with ROT13 or ROT47 method"""
        decrypted: str = ""
        for char in cipher_text:
            if char == " ":
                decrypted += " "
            elif char.isupper():
                decrypted += chr((ord(char) - self.rot - 65 + 26) % 26 + 65)
            else:
                decrypted += chr((ord(char) - self.rot - 97 + 26) % 26 + 97)

    # def encrypt_rot13(self) -> None:
    #     self.encrypt(self.ROT13)
    #
    # def encrypt_rot47(self) -> None:
    #     self.encrypt(self.ROT47)
    #
    # def decrypt_rot13(self) -> None:
    #     self.decrypt(self.ROT13)
    #
    # def decrypt_rot47(self) -> None:
    #     self.decrypt(self.ROT47)
