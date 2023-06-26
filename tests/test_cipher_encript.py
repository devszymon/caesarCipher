from funcionality.main import CaesarEncryption

def test_should_return_shifted_string_for_lowercase_letters():
    text = "abc"
    shift = 2
    encrypt = CaesarEncryption()
    assert encrypt.encrypt(text, shift) == "cde"



def test_should_return_shifted_string_for_uppercase_and_lowercase_letters():
    text = "AbCdEfGHHh"
    shift = 3
    encrypt = CaesarEncryption()

    assert encrypt.encrypt(text, shift) == "DeFgHiJKKk"



test_should_return_shifted_string_for_lowercase_letters()
test_should_return_shifted_string_for_uppercase_and_lowercase_letters()