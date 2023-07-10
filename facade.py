import datetime

from exceptions.shift_lesser_than_0 import ShiftLowerThan0
from functions.decrypt_from_json import DecryptJson
from functions.decrypter import Decrypter
from functions.encrypt_from_json import EncryptJson
from functions.encrypter import Encrypter
from functions.read_json import ReadJson


def logger_decorator(func):
    def wrapper(self, *args, **kwargs):
        # Logging information about the function call
        timestamp = datetime.datetime.now()
        function_name = func.__name__
        log_message = f"[{timestamp}] Function '{function_name}' called"

        # Saving the log message to history
        self._history.append(log_message)

        # Call the original function
        return func(self, *args, **kwargs)

    return wrapper


class Facade:
    def __init__(self):
        self.__is_running = True
        self._history = []
        self.choices = {
            1: self._encrypt_text,
            2: self._decrypt_text,
            3: self._encrypt_from_json,
            4: self._decrypt_from_json,
            5: self._save_to_file,
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
        5. Save all operations to file
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

    @logger_decorator
    def _encrypt_text(self):
        user_text = input("Enter your text: ")
        shift = self._get_shift()
        try:
            encrypted_text = Encrypter.encrypt_text(text=user_text, shift=shift)
        except ShiftLowerThan0:
            print("Shift value must be higher than 0")
            # logging error
        else:
            print(f"Your encrypted text is: {encrypted_text}")
            # self._history.append((user_text, encrypted_text, shift))

    @logger_decorator
    def _decrypt_text(self):
        user_text = input("Enter your text: ")
        shift = self._get_shift()
        decrypted_text = Decrypter.decrypt_text(text=user_text, shift=shift)
        print(f"Your decrypted text is: {decrypted_text}")
        # self._history.append((user_text, decrypted_text, shift))

    @logger_decorator
    def _encrypt_from_json(self):
        user_file = input("Enter the name of the json file: ")
        converted_data = ReadJson.read_json(user_file)
        encrypted_text = EncryptJson.encrypt_from_json(data=converted_data)
        print(f"Encrypted word/words from json is/are: {encrypted_text}")
        # self._history.append(
        #     (
        #         "Encryption from json",
        #         converted_data,
        #         encrypted_text,
        #         "shown before",
        #     )
        # )

    @logger_decorator
    def _decrypt_from_json(self):
        user_file = input("Enter the name of the json file: ")
        converted_data = ReadJson.read_json(user_file)
        decrypted_text = DecryptJson.decrypt_from_json(data=converted_data)
        print(f"Encrypted word/words from json is/are: {decrypted_text}")
        # self._history.append(
        #     (
        #         "Encryption from json",
        #         converted_data,
        #         decrypted_text,
        #         "shown before",
        #     )
        # )

    def return_history(self):
        history = []
        for operation in self._history:
            history.append(" ".join(str(element) for element in operation))
        return history

    def _save_to_file(self):
        user_file = input("Enter name of the file you want to save: ")
        with open(user_file, "w") as f:
            for _ in self.return_history():
                f.write(f"{datetime.datetime.now()}\n")
                f.write(_)
                f.write("\n")

    def _show_error(self):
        raise Exception("Something went wrong")

    def _close_app(self):
        quit()

    def _get_shift(self):
        try:
            shift = int(input("Enter number of shift (max: 31): "))
        except ValueError:
            shift = 0
        return shift


def main():
    Facade()


if __name__ == "__main__":
    main()
