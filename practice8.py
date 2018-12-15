#1
class MySuppress:
    def __init__(self, error):
        self.error = error
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.error == exc_type:
            return True
        else:
            return False

with MySuppress(KeyError):
    {}['key']

with MySuppress(KeyError):
    list_test = [12, 45, 4]
    list_test[5]

#1 better
class MySuppress:
    def __init__(self, error):
        self.error = error
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.error)

with MySuppress(KeyError):
    {}['key']

with MySuppress(KeyError):
    list_test = [12, 45, 4]
    list_test[5]

#2
class Opened:
    def __init__(self, name_of_file, mode):
        self.handle = open(name_of_file, mode)
    def __enter__(self):
        print("!!!")
        return self.handle
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.handle.close()

with Opened('file.txt', mode = 'a') as o_file:
    o_file.write("Hello")

#3
class Opened:
    def __init__(self, name_of_file, mode):
        self.name_of_file = name_of_file
        self.mode = mode
        if not self.name_of_file or self.mode:
            raise ValueError('name or mode should not be empty'.format(self.name_of_file, self.mode))

    def __enter__(self):
        self.handle = open(self.name_of_file, self.mode)
        return self.handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.handle.close()


with Opened('file.txt', mode='a') as o_file:
    o_file.write("Hello")
