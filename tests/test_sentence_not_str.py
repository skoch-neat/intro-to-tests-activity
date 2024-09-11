from main import count_a_letter
import pytest

def test_sentence_not_str():
    letter = 'a'
    sentence = True

    with pytest.raises(TypeError):
        count_a_letter(sentence, letter)