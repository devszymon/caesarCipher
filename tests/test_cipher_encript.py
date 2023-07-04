import pytest

from exceptions import shift_lesser_than_0
from facade import Encrypter


@pytest.mark.parametrize(
    "text_to_encrypt, shift, expected_text",
    [
        ("kaPp3a", 3, "ndSs3d"),
        ("1352", 3, "1352"),
        ("", 3, ""),
        ("1 dsa 02k LT!#@a", 2, "1 fuc 02m NV!#@c"),
    ],
)
def test_should_return_shifted_string_for_uppercase_and_lowercase_letters(
    text_to_encrypt, shift, expected_text
):
    actual_text = Encrypter.encrypt_text(text_to_encrypt, shift)

    assert actual_text == expected_text


#  decrypter.py używa wartość shift na minusie, więc ten test dla decryp nie ma sensu
# def test_should_raise_error_when_shift_value_is_lesser_than_0():
#     with pytest.raises(shift_lesser_than_0.ShiftLowerThan0):
#         Encrypter.encrypt_text("abc", -1)
