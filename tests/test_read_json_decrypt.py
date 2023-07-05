import pytest

from facade import DecryptJson


@pytest.mark.parametrize(
    "data_to_decrypt, expected_text",
    [
        ([{"word": "zAb231dsa", "shift": 3}], "wXy231apx"),
        (
            [{"word": "1 dsa 02k LT!#@a", "shift": 4}, {"word": "kaPp3a", "shift": 15}],
            "1 zow 02g HP!#@w, vlAa3l",
        ),
    ],
)
def test_should_return_shifted_strings_from_json_file(data_to_decrypt, expected_text):
    actual_text = DecryptJson.decrypt_from_json(data_to_decrypt)

    assert actual_text == expected_text
