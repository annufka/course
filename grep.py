import functools
import time
import io

def coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g()
        next(gen)
        return gen
    return inner


@coroutine
def grep(*args):
    what_we_find = args
    while True:
        line = (yield)
        if what_we_find in line:
            printer.send(line)
            
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


@coroutine
def dispenser(*args):
    while True:
        item = (yield)
        for target in args:
            grep.send(item)


def follow(*args):
    thefile, thefunc = args
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if line == None:
            time.sleep(.5)
        else:
            thefunc.send(line)
        
    


f_open = io.StringIO('''first line python
second line
third python
fourth
fifth''')
follow(f_open,
       # делегируем ивенты
       dispenser([
            grep('python', printer()), # отслеживаем  
            grep('is', printer()),     # заданные
            grep('great', printer()),  # сигнатуры
       ])
       )
       
f_open.write('''first line python
second line
third python
fourth
fifth''')

f_open.write('''first line python
second line
third python
python
python line''')
