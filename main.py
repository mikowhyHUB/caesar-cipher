from dataclasses import dataclass
import string


class Cipher:

    def encrypt(self, plain_text: str) -> str:
        n = 13
        encrypted = ""
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                encrypted += " "
            elif plain_text[i].isupper():
                encrypted += chr((ord(plain_text[i]) + n - 65) % 26 + 65)
            else:
                encrypted += chr((ord(plain_text[i]) + n - 97) % 26 + 97)
        return encrypted

    def decrypt(self, cipher_text: str) -> str:
        alphabet = string.ascii_lowercase
        n = 13
        decrypted_message = ""
        for char in cipher_text.lower():
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - n) % 26
                new_char = alphabet[new_pos]
                decrypted_message += new_char
            else:
                decrypted_message += char
        return decrypted_message


class FileHandler:
    pass


class Buffer:
    pass


@dataclass
class Menu:
    pass
    # menu_options: dict = {1: '...', 2: '...', 3: '...'}
    #
    # def show(self):
    #     pass


class Manager:
    pass


def main():
    test = Cipher()
    print(test.encrypt('ala ma kota'))
    print(test.decrypt('Nyn Zn xbgn'))


if __name__ == '__main__':
    main()
