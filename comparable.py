import functools


def comparable(cls):
    # magic
    class Wrapper:
        def __eq__(self, other):
            def __init__(self, *args):
                super().__init__(*args)
            return self.args == other.args

        def __ne__(self, other):
            def __init__(self, *args):
                super().__init__(*args)
            return self.args != other.args

        def __lt__(self, other):
            def __init__(self, *args):
                super().__init__(*args)
            return self.args < other.args

        def __le__(self, other):
            def __init__(self, *args):
                super().__init__(*args)
            return self.args <= other.args

        def __gt__(self, other):
            def __init__(self, *args):
                super().__init__(*args)
            return self.args > other.args

        def __ge__(self, other):
            def __init__(self, *args):
                super().__init__(*args)
            return self.args >= other.args

        # magic

    return Wrapper


@comparable
class Worker:
    """
    класс, который просто принимает значение и ничегошеньки не делает
    """
    def __init__(self, value):
        self.value = value

worker1 = Worker()
worker1 = 6
worker2 = Worker()
worker2 = 2
worker3 = Worker()
worker3 = 1
worker4 = Worker()
worker4 = 6
print(worker1 < worker2)  # False
print(worker3 < worker2)  # True
print(worker1 != worker2)  # True
print(worker1 == worker2)  # False
print(worker1 <= worker2)  # False
print(worker1 >= worker2)  # True
print(worker1 == worker4)  # True
