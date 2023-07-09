import pytest

from exceptions import shift_lesser_than_0
from facade import Decrypter


# @freeze_time('2023-08-02 12:00:00')
@pytest.mark.parametrize(
    "text_to_decrypt, shift, expected_text",
    [
        ("cde", 2, "abc"),
        ("XyZ", 1, "WxY"),
        ("", 3, ""),
        ("Lipps Asvph!", 4, "Hello World!"),
    ],
)
def test_should_return_decrypted_string_for_letters_and_numbers(
    text_to_decrypt, shift, expected_text
):
    actual_text = Decrypter.decrypt_text(text_to_decrypt, shift)

    assert actual_text == expected_text


def test_should_raise_error_when_shift_value_is_lesser_than_0():
    with pytest.raises(shift_lesser_than_0.ShiftLowerThan0) as exc:
        Decrypter.decrypt_text("abc", -1)

    print(exc)


# def test_should_raise_error_when_shift_value_is_lesser_than_0(): jak to zrobic
#     with pytest.raises(shift_lesser_than_0.ShiftLowerThan0):
#         Decrypter.decrypt_text("abc", -1)
