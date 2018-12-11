from itertools import islice

def dummy_grouper(data, n):
    begin, end = 0, n
    for element in range(len(data) // n):
        yield tuple(islice(data, begin, end))
        begin, end = begin+n, end+n

print(list(dummy_grouper(range(100), 10)))
