import string

from exceptions import shift_lesser_than_0

LETTER_RANGE = 26
LETTERS_LOWERCASE = list(string.ascii_lowercase)
LETTERS_UPPERCASE = list(string.ascii_uppercase)


class Encrypter:
    @staticmethod
    def encrypt_text(text: str, shift: int) -> str:
        new_text = ""
        # if shift < 0:
        #     raise shift_lesser_than_0.ShiftLowerThan0
        for char in text:
            if char in LETTERS_LOWERCASE:
                index = LETTERS_LOWERCASE.index(char)
                new_index = index + shift

                if new_index >= LETTER_RANGE:
                    new_index = new_index - LETTER_RANGE
                new_text += LETTERS_LOWERCASE[new_index]
            elif char in LETTERS_UPPERCASE:
                index = LETTERS_UPPERCASE.index(char)
                new_index = index + shift

                if new_index >= LETTER_RANGE:
                    new_index = new_index - LETTER_RANGE
                new_text += LETTERS_UPPERCASE[new_index]
            else:
                new_text += char

        return new_text
