# from typing import *
import string


LETTERS_LOWERCASE = list(string.ascii_lowercase)
LETTERS_UPPERCASE = list(string.ascii_uppercase)

class CaesarEncryption:
    def __init__(self):
        pass

    def encrypt(self, text: str, shift: int):
        new_text = ""

        for char in text:
            if char in LETTERS_LOWERCASE:
                index = LETTERS_LOWERCASE.index(char)
                new_index = index + shift
                new_text += LETTERS_LOWERCASE[new_index]
            else:
                index = LETTERS_UPPERCASE.index(char)
                new_index = index + shift
                new_text += LETTERS_UPPERCASE[new_index]

        return new_text

#  DODAĆ OSTATNIE LITERY Z ITD Z DUZYM SHIFTEM