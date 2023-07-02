from funcionality.main import CaesarMethods


def test_should_return_shifted_strings_from_json_file():
    data = [{"word": "mwniofinwe", "shift": 2}, {"word": "testds123", "shift": 2}]

    expected_result = ["oypkqhkpyg", "vguvfu123"]
    caesar = CaesarMethods()

    assert caesar.encrypt_from_json(data) == ", ".join(expected_result)


test_should_return_shifted_strings_from_json_file()
