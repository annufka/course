"""
1. Cделать список  N-й вложенности плоским, например:
def flatten([1,2,3, [4,5,6, [7,8,9]], 10]) -> [1,2,3,4,5,6,7,8,9,10]
"""


def flatten(list_before: list, list_after=[]) -> list:
    """
    This function unpacks nested lists.
    """
    for item in range(len(list_before)):
        if type(list_before[item]) == list:
            flatten(list_before[item])
        else:
            list_after.append(list_before[item])
    return list_after


print(flatten([1, 2, 3, [4, 5, 6, [7, 8, 9]], 10]))

"""
Попытка №2
"""

def flatten(list_before: list) -> list:
    """
    This function unpacks nested lists.
    """
    list_before = str(list_before)
    list_before = list_before.replace('[', '').replace(']', '').replace(' ', '')
    list_before = list_before.split(',')
    return [item for item in range(len(list_before))]


print(flatten([1, 2, 3, [4, 5, 6, [7, 8, 9]], 10]))
print(flatten([1, 2, 3]))
print(flatten([1, 2, [3, 4]]))


'''
Попытка 3
'''
def flatten(list_before: list) -> list:
    """
    This function unpacks nested lists.
    """
    listIsNested = True

    while listIsNested:
        keepChecking = False
        list_after = []
        for item in list_before:
            if type(item) == int:
                list_after.append(item)
            else:
                list_after.extend(item)
                keepChecking = True

        listIsNested = keepChecking  # determine if outer loop exits
        list_before = list_after[:]
    return list_after


print(flatten([1, 2, 3, [4, 5, 6, [7, 8, 9]], 10]))


"""
2. Реализовать функцию `take(n, iterable)` которая возвщарает первые `n` элементов от итерируемого.
"""


def take(n: int, iterable):
    """
    This function return first n elements of iterable.
    """
    if type(iterable) == dict:
        return {key:iterable.get(key) for key in range(1, n+1)}
    return iterable[:n]


print(take(5, [2, 4, 7, 2, 57, 8, 2, 57, 5, 6]))
print(take(2, 'dfecfdbgn'))
print(take(3, (2, 35, 2, 58, 96, 5, 0)))
print(take(2, {2:4, 5:2, 3:1, 1:0}))


"""
3. Реализовать `zip`. 
"""

def zip(first, second, third):
    """
    This function return list with n-tuples.
    """
    result = []
    min_len = min(len(first), len(second), len(third))
    for item in range(min_len):
        result_tuple = first[item], second[item], third[item]
        result.append(result_tuple)
    return result


print(zip([1243,563,35], range(4), (2,7,1,58,4)))

"""
4. Реализовать `zip` с помощью `map`.
"""


def zip(first, second, third):
    """
    This function return list with n-tuples.
    """
    result = []
    result_tuple = first, second, third
    result.append(result_tuple)
    return result


print(list(map(zip, [1243, 563, 35], range(4), (2, 7, 1, 58, 4))))

'''
Try 2
'''
def zip(*first):
    """
    This function return list with n-tuples.
    """
    return list(map(lambda *first:first, *first))


print(zip([1243, 563, 35], range(4), (2, 7, 1, 58, 4)))