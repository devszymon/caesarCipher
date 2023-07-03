import pytest

from exceptions import shift_lesser_than_0
from facade import Decrypter


# @freeze_time('2023-08-02 12:00:00')
@pytest.mark.parametrize(
    "text_to_decrypt, shift, expected_text",
    [
        ("cde", 2, "abc"),
        ("abc", 0, "abc"),
        ("abc", -1, "bcd"),
        ("", 3, ""),
    ],
)
def test_should_return_decrypted_string_for_lowercase_and_uppercase_letters(
    text_to_decrypt, shift, expected_text
):
    actual_text = Decrypter.decrypt_text(text_to_decrypt, shift)

    assert actual_text == expected_text


# def test_should_raise_error_when_shift_value_is_lesser_than_0():
#     with pytest.raises(shift_lesser_than_0.ShiftLowerThan0):
#         Decrypter.decrypt_text("abc", -1)
