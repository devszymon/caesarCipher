from exceptions.shift_lesser_than_0 import ShiftLowerThan0
from functions.encrypter import Encrypter


class Decrypter:
    @staticmethod
    def decrypt_text(text: str, shift: int):
        if shift < 0:
            raise ShiftLowerThan0
        shift = -shift % 26
        return Encrypter.encrypt_text(text=text, shift=shift)
