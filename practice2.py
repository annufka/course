#1
def map(my_function, args):
    result = []
    for item in args:
        result.append(my_function(args[item]))
    return result

map(lambda x:x*2, range(10))

#2
def map(my_function, *args):
    result = []
    for item in args:
        result.append(my_function(args[item]))
    return result

map(lambda x:x*2, *range(10))

#3
def filter(*args, my_func = None):
    result = []
    for item in args:
        if my_func:
            if my_func[item]:
                result.append(item)
        else:
            if bool(item):
                result.append(item)
    return result

filter(lambda x:x>0, [-1,-2,3,4])

#4
a = [*[1,2,3], *[4,5,6], *[8,9,10]]
*a, last = a
last
#10
*rest, (*rest, last) =  [[1,2,3], [4,5,6], [8,9,10]]
last
#10
*a, last = [*[1,2,3], *[4,5,6], *[8,9,10]]
last
#10
#*rest - то что нам не нужно, мы откинем

#5
word_list = ['aadvc', 'fhl', 'a93', ';lkhw', '2nk', 'a']
[word for word in word_list if word.startswith('a')]

#6
def is_sum_of_two(*args, result = 4):
    my_list = list(args)
    for item in range(len(my_list)):
        x = result - my_list[item]
        if item == 0:
            b = my_list[item+1:]
            n = b.count(x)
            if n != 0:
                return True
        else:
            b = my_list[item+1:]
            a = my_list[:item]
            n = b.count(x)
            m = a.count(x)
            if n != 0 or m != 0:
                return True
    return False

is_sum_of_two(*[0,6,3,2,1])

#7 as 6
def is_sum_of_two(iterable, n):
    for item in iterable:
        iterable.remove(item)
        if n-item in iterable:
            return True
        iterable.append(item)
    return False

a = [1,24,5,6,1,2]
is_sum_of_two(a, 4)

#8
cash = dict() 
def sum(*value): 
    s = 0 
    for item in range(len(value)): 
        s += value[item] 
    cash[value] = s 
    return cash
 
sum(*[1, 3, 67, 2])
#{(1, 3, 67, 2): 73}
sum(5)
#{(1, 3, 67, 2): 73, (5,): 5}

#9
cash = dict()
def sum(*value):
    
    s = 0
    if cash.get(value):
        return cash[value]
    else:
        for item in range(len(value)):
            s += value[item]
        cash[value] = s
    return cash[value]
sum(*[1, 3, 67, 2])

sum(5)

sum(*[1,5,8])

sum(5)

#10
def pol(string):
    string = str(string)
    if string[:] == string[::-1]:
        return True
    return False
    
pol('asdffdsa')




