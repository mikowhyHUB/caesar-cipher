import re
from buffer import Buffer, buffer1
from typing import Pattern


class Cipher(Buffer):
    """Class for cipher users text"""

    def __init__(self) -> None:
        super().__init__()
        self.ROT13: int = 13
        self.ROT47: int = 47
        self.letter_pattern: Pattern = re.compile(r"[a-zA-Z]")

    def encrypt(self, rot: int) -> None:
        """Encrypting users text with ROT13 or ROT47 method"""
        encrypted: str = ""
        plain_text: str = input("What text would you like to encrypt: ")
        for char in plain_text:
            if char == " ":
                encrypted += " "
            elif self.letter_pattern.match(char):
                if char.isupper():
                    encrypted += chr((ord(char) + rot - 65) % 26 + 65)
                else:
                    encrypted += chr((ord(char) + rot - 97) % 26 + 97)
            else:
                encrypted += char
        buffer1.name, buffer1.status, buffer1.rot = encrypted, "encrypted", f"ROT{rot}"

    def decrypt(self, rot: int) -> None:
        """Decrypting users text with ROT13 or ROT47 method"""
        decrypted: str = ""
        cipher_text: str = input("What text would you like to decrypt: ")
        for char in cipher_text:
            if char == " ":
                decrypted += " "
            elif char.isupper():
                decrypted += chr((ord(char) - rot - 65 + 26) % 26 + 65)
            else:
                decrypted += chr((ord(char) - rot - 97 + 26) % 26 + 97)
        buffer1.name, buffer1.status, buffer1.rot = decrypted, "decrypted", f"ROT{rot}"

    def encrypt_rot13(self) -> None:
        self.encrypt(self.ROT13)

    def encrypt_rot47(self) -> None:
        self.encrypt(self.ROT47)

    def decrypt_rot13(self) -> None:
        self.decrypt(self.ROT13)

    def decrypt_rot47(self) -> None:
        self.decrypt(self.ROT47)
