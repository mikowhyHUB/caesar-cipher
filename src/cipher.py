from typing import Any


class Cipher:
    """Class for cipher users text"""

    # def __init__(
    #         self,
    #         rot: None,
    #         text: str,
    # ) -> None:
    #     self.rot = rot
    #     self.text = text

    @staticmethod
    def encrypt(rot: Any, plain_text: str) -> str:
        """Encrypting users text with ROT13 or ROT47 method"""
        encrypted: str = ""
        for char in plain_text:
            if char == " ":
                encrypted += " "
            elif char.isalpha():
                if char.isupper():
                    encrypted += chr((ord(char) + rot - 65) % 26 + 65)
                else:
                    encrypted += chr((ord(char) + rot - 97) % 26 + 97)
            else:
                encrypted += char
        return encrypted

    @staticmethod
    def decrypt(rot: Any, cipher_text: str) -> str:
        """Decrypting users text with ROT13 or ROT47 method"""
        decrypted: str = ""
        for char in cipher_text:
            if char == " ":
                decrypted += " "
            elif char.isupper():
                decrypted += chr((ord(char) - rot - 65 + 26) % 26 + 65)
            else:
                decrypted += chr((ord(char) - rot - 97 + 26) % 26 + 97)
        return decrypted
