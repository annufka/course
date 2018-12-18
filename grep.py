import functools
import time

def coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def grep(what_we_find, func):
    while True:
        line = (yield)
        if what_we_find in line:
            func.send(line)
            
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)

@coroutine
def dispenser(func):
    while True:
        line = (yield)
        for one_func in func:
            one_func.send(line)

def follow(thefile, thefunc):
    thefile.seek(0, 2)
    while True:
        try:
            line = thefile.readline()
        except:
            time.sleep(5)
        else:
            thefunc.send(line)
        
        

f_open = open('log.txt', 'r') # подключаемся к файлу
follow(f_open,
       # делегируем ивенты
       dispenser([
           grep('python', printer()), # отслеживаем  
           grep('is', printer()),     # заданные
           grep('great', printer()),  # сигнатуры
       ])
       )
