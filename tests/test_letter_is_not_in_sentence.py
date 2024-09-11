from main import count_a_letter
import pytest

def test_letter_not_in_sentence():
    letter = 'x'
    sentence = 'I have a banana'

    result = count_a_letter(sentence, letter)

    assert result == 0