from itertools import islice
def dummy_grouper(data, n):
    begin = 0
    end = n
    for i in range(len(data)//n):
        yield tuple(islice(data, begin, end))
        begin += n
        end +=n
    
print(list(dummy_grouper(range(100000000), 10)))
