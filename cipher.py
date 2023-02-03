import string
from buffer import Buffer, buffer1


class Cipher(Buffer):
    """Class for cipher users text"""

    def __init__(self) -> None:
        super().__init__()
        self.ROT13 = 13
        self.ROT47 = 47

    def encrypt_rot13(self) -> None:
        """Encrypting users text with ROT13 method"""
        encrypted = ""
        plain_text = input("What text would you like to encrypt: ")
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + self.ROT13 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + self.ROT13 - 97) % 26 + 97)
        buffer1.name, buffer1.status, buffer1.rot = encrypted, "encrypted", "ROT13"

    def encrypt_rot47(self) -> None:
        """Encrypting users text with ROT47 method"""
        encrypted = ""
        plain_text = input("What text would you like to encrypt: ")
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + self.ROT47 - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + self.ROT47 - 97) % 26 + 97)
        buffer1.name, buffer1.status, buffer1.rot = encrypted, "encrypted", "ROT47"

    def decrypt_rot13(self) -> None:
        """Decrypting users text with ROT13 method"""
        alphabet = string.ascii_lowercase
        decrypted = ""
        cipher_text = input("What text would you like to decrypt: ")
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - self.ROT13) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        buffer1.name, buffer1.status, buffer1.rot = decrypted, "decrypted", "ROT13"

    def decrypt_rot47(self) -> None:
        """Decrypting users text with ROT47 method"""
        alphabet = string.ascii_lowercase
        decrypted = ""
        cipher_text = input("What text would you like to decrypt: ")
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - self.ROT47) % 26
                new_char = alphabet[new_pos]
                decrypted += new_char
            else:
                decrypted += char
        buffer1.name, buffer1.status, buffer1.rot = decrypted, "decrypted", "ROT47"
