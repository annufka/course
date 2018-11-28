import functools

def comparable(cls):
    """
    Декоратор ласса, который служит для сравнения экземпляров класса
    """
    #копируем всю информацию о классе
    @functools.wraps(cls)
    def inner(*args):
        #присваиваем полученное значение
        value = args
        #возвращаем значение
        return value
    return inner

@comparable
class Worker:
    """
    класс, который просто принимает значение и ничегошеньки не делает
    """
    def __init__(self, value: int):
        self.value = value

worker1 = Worker(6)
worker2 = Worker(2)
worker3 = Worker(1)
worker4 = Worker(6)
print(worker1 < worker2)#False
print(worker3 < worker2)#True
print(worker1 != worker2)#True
print(worker1 == worker2)#False
print(worker1 <= worker2)#False
print(worker1 >= worker2)#True
print(worker1 == worker4)#True
