import datetime
import json
import string

LETTERS_LOWERCASE = list(string.ascii_lowercase)
LETTERS_UPPERCASE = list(string.ascii_uppercase)


# class JsonMethods:
#     def __init__(self):
#         pass
#
#     def read_json(self, file_name: str) -> dict:
#         with open(file_name, "r") as json_file:
#             data = json.load(json_file)
#
#         return data


# jak to fajnie testować?


class CaesarMethods:
    def __init__(self):
        self.cipher_dict = {}

    def encrypt(self, text: str, shift: int) -> str:
        new_text = ""

        for char in text:
            if char in LETTERS_LOWERCASE:
                index = LETTERS_LOWERCASE.index(char)
                new_index = index + shift
                if new_index >= 26:
                    new_index = new_index - 26
                new_text += LETTERS_LOWERCASE[new_index]
            elif char in LETTERS_UPPERCASE:
                index = LETTERS_UPPERCASE.index(char)
                new_index = index + shift
                if new_index >= 26:
                    new_index = new_index - 26
                new_text += LETTERS_UPPERCASE[new_index]

            else:
                new_text += char
        self.cipher_dict.update({text: new_text})
        return new_text

    def decrypt(self, text: str, shift: int) -> str:
        return self.encrypt(text, -shift)

    def read_json(self, file_name: str) -> dict:
        with open(file_name, "r") as json_file:
            data = json.load(json_file)

        return data

    def encrypt_from_json(self, data) -> list:
        encrypted = []
        for dictionary in data:
            dictionary_values = list(dictionary.values())
            encrypted_text = self.encrypt(dictionary_values[0], dictionary_values[1])
            encrypted.append(encrypted_text)

        return encrypted


class CaesarCipherFacade:
    def __init__(self):
        self.cipher = CaesarMethods()
        self.history = []

    def encrypt_text(self, text: str, shift: int):
        encrypted = self.cipher.encrypt(text, shift)
        self.history.append(("Encryption", text, encrypted, shift))
        return self.cipher.encrypt(text, shift)

    def decrypt_text(self, text: str, shift: int):
        decrypted = self.cipher.decrypt(text, shift)
        self.history.append(("Decryption", text, decrypted, shift))
        return self.cipher.decrypt(text, shift)

    def save_results(self, file):
        with open(file, "w") as f:
            for method, before, text, shift in self.history:
                f.write(f"{datetime.datetime.now()}\n")
                f.write(
                    f"{method}: Text before: {before} | Text after:  {text} (shift:"
                    f" {shift})\n\n"
                )

    def encrypt_from_json(self, data):
        return self.cipher.encrypt_from_json(self.cipher.read_json(data))


def display_menu():
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Save all logs to file")
    print("4. Encrypt from Json file")
    print("9. Close app")


def get_choice():
    choice = input("Choose option by typing corresponding number: ")
    return choice


def main():
    cipher = CaesarCipherFacade()
    display_menu()
    while True:
        choice = get_choice()
        if choice == "1":
            text = input("Enter your text: ")
            shift = int(input("Enter number of shift: "))
            print(f"Your encrypted text is: {cipher.encrypt_text(text, shift)}")
        elif choice == "2":
            text = input("Enter your text: ")
            shift = int(input("Enter number of shift: "))
            print(f"Your decrypted text is: {cipher.decrypt_text(text, shift)}")
        elif choice == "3":
            file_choice = input("Enter the name of the file with results: ")
            cipher.save_results(file_choice)
            print("Results saved successfully.")
        elif choice == "4":
            file_choice = input("Enter the name of the json file: ")
            print(f"Encrypted from json is: {cipher.encrypt_from_json(file_choice)}")

        elif choice == "9":
            print("Stopping app.")
            quit()
        else:
            print("Wrong choice")

        display_menu()


if __name__ == "__main__":
    main()
