import string

LETTERS_LOWERCASE = list(string.ascii_lowercase)
LETTERS_UPPERCASE = list(string.ascii_uppercase)


class CaesarMethods:
    def __init__(self):
        pass

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

        return new_text

    def decrypt(self, text: str, shift: int) -> str:
        return self.encrypt(text, -shift)


class CaesarCipherFacade:
    def __init__(self):
        self.cipher = CaesarMethods()

    def encrypt_text(self, text: str, shift: int):
        return self.cipher.encrypt(text, shift)

    def decrypt_text(self, text: str, shift: int):
        return self.cipher.decrypt(text, shift)


def display_menu():
    print("1. Encrypt text")
    print("2. Decrypt text")


def get_choice():
    choice = input("Choose option by typing corresponding number: ")
    return choice


def main():
    cipher = CaesarCipherFacade()
    display_menu()
    choice = get_choice()

    if choice == "1":
        text = input("Enter your text: ")
        shift = int(input("Enter number of shift: "))
        print(f"Your encrypted text is: {cipher.encrypt_text(text, shift)}")
    elif choice == "2":
        text = input("Enter your text: ")
        shift = int(input("Enter number of shift: "))
        print(f"Your decrypted text is: {cipher.decrypt_text(text, shift)}")
    else:
        print("Wrong choice")


if __name__ == "__main__":
    main()
