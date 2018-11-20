import string

en_alphabet = string.ascii_lowercase
ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def abc(my_secret_key: str) -> int:
    """
    It function return shift. Shift is the sum of 1,2,3
    """
    shift = 0
    for letter in my_secret_key:
        if letter in en_alphabet[0:9]:
            shift += 1
        elif letter in en_alphabet[9:20]:
            shift += 2
        elif letter in en_alphabet[20:25]:
            shift += 3
    return shift


def encode(my_text_input: str, my_secret_key: str) -> str:
    """
    Function for encode some text
    """
    shift = abc(my_secret_key)
    for letter_in_text in range(len(my_text_input)):
        if my_text_input[letter_in_text] == ' ' or my_text_input[letter_in_text] in string.punctuation:
            continue
        if my_text_input[letter_in_text].lower() in en_alphabet:
            index_new_letter = en_alphabet.index(my_text_input[letter_in_text].lower()) + shift
            if index_new_letter > 25:
                index_new_letter = (index_new_letter % 25) - 1
            my_text_input = my_text_input[:letter_in_text] + (
                en_alphabet[index_new_letter] if my_text_input[letter_in_text].islower() == True else en_alphabet[
                    index_new_letter].upper()) + my_text_input[letter_in_text + 1:]
        if my_text_input[letter_in_text].lower() in ru_alphabet:
            index_new_letter = ru_alphabet.index(my_text_input[letter_in_text].lower()) + shift
            if index_new_letter > 32:
                index_new_letter = (index_new_letter % 32) - 1
            my_text_input = my_text_input[:letter_in_text] + (
                ru_alphabet[index_new_letter] if my_text_input[letter_in_text].islower() == True else ru_alphabet[
                    index_new_letter].upper()) + my_text_input[letter_in_text + 1:]
    return my_text_input


def decode(my_text_input, my_secret_key):
    """
    Function for decode some text
    """
    shift = abc(my_secret_key)
    for letter_in_text in range(len(my_text_input)):
        if my_text_input[letter_in_text] == ' ' or my_text_input[letter_in_text] in string.punctuation:
            continue
        if my_text_input[letter_in_text].lower() in en_alphabet:
            index_new_letter = en_alphabet.index(my_text_input[letter_in_text].lower()) - shift
            if index_new_letter < 0:
                index_new_letter = 25 + index_new_letter + 1
            my_text_input = my_text_input[:letter_in_text] + (
                en_alphabet[index_new_letter] if my_text_input[letter_in_text].islower() == True else en_alphabet[
                    index_new_letter].upper()) + my_text_input[letter_in_text + 1:]
        if my_text_input[letter_in_text].lower() in ru_alphabet:
            index_new_letter = ru_alphabet.index(my_text_input[letter_in_text].lower()) - shift
            if index_new_letter < 0:
                index_new_letter = 32 + index_new_letter + 1
            my_text_input = my_text_input[:letter_in_text] + (
                ru_alphabet[index_new_letter] if my_text_input[letter_in_text].islower() == True else ru_alphabet[
                    index_new_letter].upper()) + my_text_input[letter_in_text + 1:]
    return my_text_input


print(decode(encode('park', 'aku'), 'aku'))

print(decode(encode('format', 'my key'), 'my key'))

print(decode(encode('where are you, Poul?', 'my key'), 'my key'))

print(decode(encode('фырФЫрФыр', 'aku'), 'aku'))
