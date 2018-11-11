"""
Проверить строку в виде пароля на предмет прохождения условий:
-символы в верхнем регистре,
-символы в нижнем регистре,
-цифры,
-длина строки более 8 символов
```check_password('Som@Pa55word!') -> True
check_password('123q') -> False```
"""

def check_password(user_input):
    if len(user_input) > 8 and any(item.isdigit() for item in user_input) == True and any(
            item.isupper() for item in user_input) == True and any(item.islower() for item in user_input) == True:
        return True
    return False


print(check_password('Som@Pa55word!'))
print(check_password('123q'))


"""
Реализовать функцию конструктор, задающую параметры для определения границ расчета элементов, которая в свою очередь будет возвращать функцию для вычисления минимального элемента в последовательности

Задаем границы для функции find_min, которую возвращает функция min_in_range
```find_min = min_in_range(from=0, to=500)```
```find_min(-1, 1, 2) -> 0```
находим минимальный элемент в последовательности: минимальный элемент `-1` выходит за рамки, так что возвращается близжайшее граничное значение `(from=0)`
```find_min(1,2,3,4,5) -> 1```
```find_min(*[15,20,40]) ->15```
"""

def find_min(*args):
    my_list = []
    for item in args:
        if int(item) >= 0 and int(item) <= 500:
            my_list.append(item)
    return min(my_list)

print(find_min(-1, 1, 2))
print(find_min(1,2,3,4,5))
print(find_min(*[15,20,40]))