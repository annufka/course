'''
test = 'abcdd'
test.isdigit() - все ли элементы числа
test.isalpha() - есть ли число
test.startswith('')- проверить начинается ли слово с определенного элемента
test.split - возвращает список из строк
'''
#1
result = list()
    for letter in test:
	result.append(letter)
	
print(result)
#['a', 'b', 'c', 'd', 'd']

#2
for letter in test:
	if letter == 'a' or letter == 'd':
		result.append(letter)

#3
numbers = '123456789'
result = []
for i in range(len(numbers)):
	if int(numbers[i])%2 ==0:
		result.append(numbers[i])

		
print(result)
#['2', '4', '6', '8']
print(''.join(result))
#2468

x = set([1,2,3,4,5])
y = set([4,5,6,7,8])
y-x
y.difference(x)
#{8, 6, 7}

#set не гарантирует порядок возвращения

result_dict = {}
result_dict['even'] = []
result_dict['odd'] = []
result_dict
#{'even': [], 'odd': []}
for number in range(100):
    if number%2 == 0:
	    result_dict['even'].append(number)
    else:
	    result_dict['odd'].append(number)

print(result_dict['even'])
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
print(result_dict['odd'])
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
result_dict
#{'even': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98], 'odd': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]}
sum(result_dict['even'])
#2450
sum(result_dict['odd'])
#2500
result_dict['even'] = sum(result_dict['even'])
result_dict['even']
#2450
result_dict['odd'] = sum(result_dict['odd'])
result_dict['odd']
#2500
result_dict
#{'even': 2450, 'odd': 2500}

result_dict.keys()
#dict_keys(['even', 'odd'])

other_dict.keys() & result_dict.keys()
#{'odd'} - можно делать операции как с множествами

#итерация в словарях по ключам
for key in result_dict:
	print(key, value)

#for key, value in result_dict.items(): - вернуть ключ и значение
new_dummy_dict = []
>>> new_dummy_dict = {}
for key, value in result_dict.items():
	new_dummy_dict[key] = value
	
print(key, value)
#odd 2500

dummy_dict = {1:1, 2:[], 3:3, 4:[]}
new_dummy_dict = {}
for key, value in dummy_dict.items():
    if isinstance(value, list):#проверки принадлежности данных определенному классу (типу данных)
	continue
    new_dummy_dict[key]=value

print(new_dummy_dict)
#{1: 1, 3: 3}




