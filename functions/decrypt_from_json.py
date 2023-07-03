from functions.decrypter import Decrypter


class DecryptJson:
    @staticmethod
    def decrypt_from_json(data) -> str:
        decrypted = []
        for dictionary in data:
            dictionary_values = list(dictionary.values())
            encrypted_text = Decrypter.decrypt_text(
                dictionary_values[0], dictionary_values[1]
            )
            decrypted.append(encrypted_text)
        output = ", ".join(decrypted)

        return output
