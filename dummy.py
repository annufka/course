from itertools import islice

def dummy_grouper(data, n):
    begin, end = 0, n
    for element in range(len(data) // n):
        yield tuple(islice(data, begin, end))
        begin, end = begin+n, end+n

print(list(dummy_grouper(range(100000000), 10)))


from itertools import islice

def dummy_grouper(data, n):
    groups_count = len(data) // n
    yield [tuple(islice(data, i*n, (i+1)*n)) for i in range(groups_count)]
list(dummy_grouper(range(100000000), 10))


def dummy_grouper(data, n):
    result_all = []
    for i in range(n):
        result_all.append(tuple(range(i, len(data), n)))
    return zip(*result_all)

list(dummy_grouper(range(10000000), 10))
