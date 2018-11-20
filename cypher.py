import string

en_alphabet = string.ascii_lowercase
ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def abc(my_secret_key: str) -> int:
    """
    It function return shift. Shift is the sum of 1,2,3
    """
    shift = 0
    for letter in my_secret_key:
        if letter in en_alphabet[0:9] or ru_alphabet[0:11]:
            shift += 1
        elif letter in en_alphabet[9:20] or ru_alphabet[11:21]:
            shift += 2
        elif letter in en_alphabet[20:25] or ru_alphabet[21:32]:
            shift += 3
    return shift

def encode(my_text_input: str, my_secret_key: str) -> str:
    """
    Function for encode some text
    """
    shift = abc(my_secret_key)
    for letter_in_text in range(len(my_text_input)):
        if my_text_input[letter_in_text] == ' ':
            continue
        if my_text_input[letter_in_text] in en_alphabet:
            index_new_letter = en_alphabet.index(my_text_input[letter_in_text]) + shift
            if index_new_letter > 25:
                index_new_letter = (index_new_letter % 25) - 1
            my_text_input = my_text_input[:letter_in_text] + en_alphabet[index_new_letter] + my_text_input[letter_in_text+1:]
        if my_text_input[letter_in_text] in ru_alphabet:
            index_new_letter = ru_alphabet.index(my_text_input[letter_in_text]) + shift
            if index_new_letter > 32:
                index_new_letter = (index_new_letter % 32) - 1
            my_text_input = my_text_input[:letter_in_text] + ru_alphabet[index_new_letter] + my_text_input[letter_in_text+1:]
    return my_text_input


def decode(my_text_input, my_secret_key):
    """
    Function for decode some text
    """
    shift = abc(my_secret_key)
    for letter_in_text in range(len(my_text_input)):
        if my_text_input[letter_in_text] == ' ':
            continue
        if my_text_input[letter_in_text] in en_alphabet:
            index_new_letter = en_alphabet.index(my_text_input[letter_in_text]) - shift
            if index_new_letter < 0:
                index_new_letter = 25 + index_new_letter + 1
            my_text_input = my_text_input[:letter_in_text] + en_alphabet[index_new_letter] + my_text_input[letter_in_text+1:]
        if my_text_input[letter_in_text] in ru_alphabet:
            index_new_letter = ru_alphabet.index(my_text_input[letter_in_text]) - shift
            if index_new_letter < 0:
                index_new_letter = 32 + index_new_letter + 1
            my_text_input = my_text_input[:letter_in_text] + ru_alphabet[index_new_letter] + my_text_input[letter_in_text+1:]
    return my_text_input

print(encode('park', 'aku'))
print(decode('vgxq', 'aku'))

print(encode('park', 'my key'))
print(decode('dofy', 'my key'))

print(encode('how are you', 'my key'))
print(decode('vck ofs mci', 'my key'))

print(encode('фырфырфыр', 'aku'))
print(decode('чюучюучюу', 'aku'))
