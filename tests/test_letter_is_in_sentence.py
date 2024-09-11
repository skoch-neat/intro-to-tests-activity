from main import count_a_letter
import pytest

def test_letter_is_in_sentence():
    letter = 'a'
    sentence = 'I have a banana'

    result = count_a_letter(sentence, letter)

    assert result == 5