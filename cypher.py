import string

alphabet = string.ascii_lowercase
def abc(my_secret_key):
    shift = 0
    for letter in my_secret_key:
        if letter in alphabet[0:9]:
            shift += 1
        elif letter in alphabet[9:20]:
            shift += 2
        else:
            shift += 3
    return shift

def encode(my_text_input, my_secret_key):
    shift = abc(my_secret_key)
    for letter_in_text in range(len(my_text_input)):
        if my_text_input[letter_in_text] == ' ':
            continue
        index_new_letter = alphabet.index(my_text_input[letter_in_text]) + shift
        if index_new_letter > 25:
            index_new_letter = (index_new_letter % 25) - 1
        my_text_input = my_text_input[:letter_in_text] + alphabet[index_new_letter] + my_text_input[letter_in_text+1:]
    return my_text_input


def decode(my_text_input, my_secret_key):
    shift = abc(my_secret_key)
    for letter_in_text in range(len(my_text_input)):
        if my_text_input[letter_in_text] == ' ':
            continue
        index_new_letter = alphabet.index(my_text_input[letter_in_text]) - shift
        if index_new_letter < 0:
            index_new_letter = 25 + index_new_letter + 1
        my_text_input = my_text_input[:letter_in_text] + alphabet[index_new_letter] + my_text_input[letter_in_text+1:]
    return my_text_input

print(encode('park', 'aku'))
print(decode('vgxq', 'aku'))

print(encode('park', 'my key'))
print(decode('dofy', 'my key'))

print(encode('how are you', 'my key'))
print(decode('vck ofs mci', 'my key'))
