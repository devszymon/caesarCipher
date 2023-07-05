import pytest

from facade import EncryptJson


@pytest.mark.parametrize(
    "data_to_encrypt, expected_text",
    [
        (
            [{"word": "mwniofinwe", "shift": 2}, {"word": "testds123", "shift": 2}],
            "oypkqhkpyg, vguvfu123",
        ),
        (
            [{"word": "1 dsa 02k LT!#@a", "shift": 2}, {"word": "kaPp3a", "shift": 3}],
            "1 fuc 02m NV!#@c, ndSs3d",
        ),
    ],
)
def test_should_return_shifted_strings_from_json_file(data_to_encrypt, expected_text):
    actual_text = EncryptJson.encrypt_from_json(data_to_encrypt)

    assert actual_text == expected_text
