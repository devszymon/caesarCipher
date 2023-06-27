from funcionality.main import CaesarMethods


def test_should_return_decrypted_string_for_lowercase_letters():
    text = "cde"
    shift = 2

    encrypt = CaesarMethods()

    assert encrypt.decrypt(text, shift) == "abc"


def test_should_return_decrypted_string_for_lowercase_and_uppercase_letters():
    text = "ZabA"
    shift = 2

    encrypt = CaesarMethods()

    assert encrypt.decrypt(text, shift) == "XyzY"

    text = "AbCdE"
    shift = 5

    encrypt = CaesarMethods()

    assert encrypt.decrypt(text, shift) == "VwXyZ"


test_should_return_decrypted_string_for_lowercase_letters()
test_should_return_decrypted_string_for_lowercase_and_uppercase_letters()
