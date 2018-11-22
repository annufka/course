import string

en_alphabet = string.ascii_lowercase


def abc(my_secret_key: str) -> int:
    """
    It function return shift. Shift is the sum of 1,2,3
    """
    #объявление переменной, которая используется для "сдвига" символов 
    shift = hash(my_secret_key) % (2**16)
    return shift


def encode(my_text_input: str, my_secret_key: str) -> str:
    """
    Function for encode some text
    """
    shift = abc(my_secret_key)
    #получим значение символа в unicode
    unicode_string = list(map(ord, my_text_input))
    for letter_in_text in range(len(unicode_string)):
        #номер нового символа
        number_new_letter = unicode_string[letter_in_text] + shift
        #если вдруг мы вышли за пределы 2**16, то начнем индексы считать сначала
        if number_new_letter > 2 ** 16:
            number_new_letter = (number_new_letter % (2 ** 16)) - 1
        #меняем в нашем списке код символа
        unicode_string[letter_in_text] = number_new_letter
    #возвращаем символы
    my_text_input = list(map(chr, unicode_string))
    #возвращаем вместо списка строку
    return str("".join(my_text_input))


def decode(my_text_input, my_secret_key):
    """
    Function for decode some text
    """
    shift = abc(my_secret_key)
    #получим значение символа в unicode
    unicode_string = list(map(ord, my_text_input))
    for letter_in_text in range(len(unicode_string)):
        #получим значение символа в unicode
        number_new_letter = unicode_string[letter_in_text] - shift
        #маловероятный случай
        if number_new_letter > 2 ** 16:
            number_new_letter = (number_new_letter % (2 ** 16)) + 1
        #меняем в нашем списке код символа
        unicode_string[letter_in_text] = number_new_letter
        #возвращаем символы
    my_text_input = list(map(chr, unicode_string))
    #возвращаем символы
    return str("".join(my_text_input))


print(decode(encode('park', 'aku'), 'aku'))

print(decode(encode('format', 'my key'), 'my key'))

print(decode(encode('where are you, Poul?', 'my key'), 'my key'))

print(decode(encode('фырФЫрФыр', 'aku'), 'aku'))
