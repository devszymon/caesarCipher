from functions.decrypt_from_json import DecryptJson
from functions.decrypter import Decrypter
from functions.encrypt_from_json import EncryptJson
from functions.encrypter import Encrypter
from functions.read_json import ReadJson


class Facade:
    def __init__(self):
        self.__is_running = True
        self.choices = {
            1: self._encrypt_text,
            2: self._decrypt_text,
            3: self._encrypt_from_json,
            4: self._decrypt_from_json,
            9: self._close_app,
        }
        self._start()

    def _start(self):
        """starting application"""
        while self.__is_running:
            self._display_menu()
            self._get_and_execute_user_choice()

    def _display_menu(self):
        menu = """
        1. Encrypt text
        2. Decrypt text
        3. Encrypt from json file
        4. Decrypt from json file
        9. Close app
        """
        print(menu)

    def _get_and_execute_user_choice(self):
        try:
            user_choice = int(input("Choose what you want do: "))
        except ValueError as e:
            print(e)
        else:
            self.choices.get(user_choice, self._show_error)()

    def _encrypt_text(self):
        user_text = input("Enter your text: ")
        shift = int(input("Enter number of shift (max: 31): "))
        encrypted_text = Encrypter.encrypt_text(text=user_text, shift=shift)
        print(f"Your encrypted text is: {encrypted_text}")

    def _decrypt_text(self):
        user_text = input("Enter your text: ")
        shift = int(input("Enter number of shift (max: 31): "))
        decrypted_text = Decrypter.decrypt_text(text=user_text, shift=shift)
        print(f"Your decrypted text is: {decrypted_text}")

    def _encrypt_from_json(self):
        user_file = input("Enter the name of the json file: ")
        converted_data = ReadJson.read_json(user_file)
        encrypted_text = EncryptJson.encrypt_from_json(data=converted_data)
        print(f"Encrypted word/words from json is/are: {encrypted_text}")

    def _decrypt_from_json(self):
        user_file = input("Enter the name of the json file: ")
        converted_data = ReadJson.read_json(user_file)
        decrypted_text = DecryptJson.decrypt_from_json(data=converted_data)
        print(f"Encrypted word/words from json is/are: {decrypted_text}")

    def _close_app(self):
        quit()

    def _show_error(self):
        raise Exception("Something went wrong")


def main():
    Facade()


if __name__ == "__main__":
    main()
