from functions.encrypter import Encrypter


class EncryptJson:
    @staticmethod
    def encrypt_from_json(data) -> str:
        encrypted = []
        for dictionary in data:
            dictionary_values = list(dictionary.values())
            encrypted_text = Encrypter.encrypt_text(
                dictionary_values[0], dictionary_values[1]
            )
            encrypted.append(encrypted_text)
        output = ", ".join(encrypted)

        return output
