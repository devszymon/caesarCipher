from functions.encrypter import Encrypter


class Decrypter:
    @staticmethod
    def decrypt_text(text: str, shift: int):
        return Encrypter.encrypt_text(text=text, shift=-shift)
