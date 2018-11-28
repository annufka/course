import functools

def comparable(cls):
    @functools.wraps(cls)
    def deco(self, func):
        def inner(self, *args, func):
            first_value, second_value = cls(*args)
            if func == '!=':
                return first_value != second_value
            elif func == '==':
                return first_value == second_value
            elif func == '>=':
                return first_value >= second_value
            elif func == '<=':
                return first_value <= second_value
            elif func == '>':
                return first_value > second_value
            elif func == '<':
                return first_value < second_value

        return deco(self, func)

    return comparable(cls)


@comparable
class Worker:
    @property
    def begin(self):
        self.first_value = first_value
        self.second_value = second_value
        self.func = func


a = Worker()
a.begin(5, 7, '==')
