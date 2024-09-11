# from main import count_a_letter
# import pytest

# def test_demo_one():
#     num_1 = 8
#     num_2 = 9

#     result = num_1 + num_2

#     assert result == 17

# def test_demo_two():
#     num_1 = 18
#     num_2 = 24

#     result = num_1 + num_2

#     assert result == 42
# Delete the demo tests and add your tests here 

# def test_verify_letter_is_in_sentence():
#     letter = 'a'
#     sentence = 'I have a banana'

#     result = count_a_letter(sentence, letter)

#     assert result == 5

# def test_verify_letter_not_in_sentence():
#     letter = 'x'
#     sentence = 'I have a banana'

#     result = count_a_letter(sentence, letter)

#     assert result == 0

# def test_letter_not_a_letter():
#     letter = 3
#     sentence = 'I have a banana'

#     with pytest.raises(AttributeError):
#         count_a_letter(sentence, letter)

# def test_sentence_not_a_sentence():
#     letter = 'a'
#     sentence = True

#     with pytest.raises(TypeError):
#         count_a_letter(sentence, letter)