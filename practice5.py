# 1
class Useless:
    def __init__(self, name):
        self.name = name


u = Useless(42)
u.name


# 2
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


u = User("Ann", "Didukh")
u.first_name
# 'Ann'
u.last_name


# 'Didukh'

# 3
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


u = User("Ann", "Didukh")
u.get_name()


# 'Ann Didukh'

# 4
class BaseUser:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class User(BaseUser):
    pass


u = User('a', 'b')
u.get_name()


# 'a b'

# 5
class BaseUser:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Admin(BaseUser):
    def __init__(self, first_name, last_name, position):
        self.position = position
        super().__init__(first_name, last_name)


a = Admin('A', 'D', 'y')
a.position
# 'y'
a.get_name()


# 'A D'

# 6
class BaseUser:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class User(BaseUser):
    pass


class Admin(User):
    def __init__(self, first_name, last_name, position):
        self.position = position
        super().__init__(first_name, last_name)

    def create_user(self, first_name, last_name):
        user = User(first_name, last_name)
        return user


a = Admin('b', 'c', 'h')
a.create_user('2', '5')


# 'b c'

# 7
class BaseUser:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class User(BaseUser):
    def __repr__(self):
        return "{}: {} {}".format(self.__class__.__name__, self.first_name, self.last_name)


class Admin(User):
    _create_user = []

    def __init__(self, first_name, last_name, position):
        self.position = position
        super().__init__(first_name, last_name)

    def create_user(self, first_name, last_name):
        user = User(first_name, last_name)
        self._create_user.append(user)
        return user

    def get_created_users(self):
        return self._create_user


a = Admin(1, 3, 5)
a.create_user(2, 5)
# User: 2 5

a.get_created_users()


# [User: 2 5]

# 8

class BaseUser:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class User(BaseUser):
    def __repr__(self):
        return "{}: {} {}".format(self.__class__.__name__, self.first_name, self.last_name)


class Admin(User):
    _create_user = []

    def __init__(self, first_name, last_name, position):
        self.position = position
        super().__init__(first_name, last_name)

    def create_user(self, first_name, last_name):
        user = User(first_name, last_name)
        self._create_user.append(user)
        return user

    def get_created_users(self):
        return self._create_user

    def get_test_name(self):
        return (('John', 'Doe'), ('Ann', 'Folue'), ('Poul', 'Goo'), ('Pite', 'Tone'))

    def generate_test_users(self):
        for first_name, last_name in self.get_test_name():
            self.create_user(first_name, last_name)

a = Admin(1,3,5)
a.create_user(2,5)
#User: 2 5
a.get_created_users()
#[User: 2 5]
a.generate_test_users()
a.get_created_users()
#[User: 2 5, User: John Doe, User: Ann Folue, User: Poul Goo, User: Pite Tone]

#9
class BaseUser:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class User(BaseUser):

    def __init__(self, first_name, last_name):
        self.friends = []
        super().__init__(first_name, last_name)

    def __repr__(self):
        return "{}: {} {}".format(self.__class__.__name__, self.first_name, self.last_name)

    def say_hello_to(self, user):
        self.friends.append(user)

    def friends(self):
        return self.friends


class GenerateMixin:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_test_name(self):
        return (('John', 'Doe'), ('Ann', 'Folue'), ('Poul', 'Goo'), ('Pite', 'Tone'))

    def generate_test_users(self):
        for first_name, last_name in self.get_test_name():
            self.create_user(first_name, last_name)


class Admin(GenerateMixin, User):
    _created_user = {}

    def __init__(self, first_name, last_name, position):
        self.position = position
        super().__init__(first_name, last_name)

    def create_user(self, first_name, last_name):
        user = User(first_name, last_name)
        self._created_user[user.get_name()] = user
        return user

    def get_created_users(self):
        return self._created_user

    def get_user(self, username):
        return self._created_user.get(username)


a = Admin(1, 2, 3)
a.generate_test_users()
john = a.get_user("John Doe")
print(john)
tom = a.get_user('Poul Goo')
john.say_hello_to(tom)
print(john.friends)

#10
class BaseUser:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class User(BaseUser):
    def __init__(self, *args):
        self.friends = []
        super().__init__(*args)

    def say_hello_to(self, user):
        self.friends.append(user)

    def __repr__(self):
        spec_str = "{}: {} {}, gender:{}, age:{}"
        return spec_str.format(self.__class__.__name__,
                               self.first_name,
                               self.last_name,
                               self.gender,
                               self.age)


class GenerateOperationsMixin:
    def get_test_names(self):
        return (('John', 'Doe', 'male', '20'),
                ('Sansa', 'Stark', 'female', '25'),
                ('Carl', 'Carlson', 'male', '25'),
                ('Thor', 'Odinson', 'male', '30'),
                ('Bruce', 'Wayne', 'male', '35'))

    def generate_test_users(self):
        for params in self.get_test_names():
            self.create_user(*params)


class Admin(GenerateOperationsMixin, User):
    _created_users = {}

    def __init__(self, first_name, last_name, position):
        self.position = position
        self.first_name = first_name
        self.last_name = last_name

    def create_user(self, *args):
        user = User(*args)
        self._created_users[user.get_name()] = user
        return user

    def get_user(self, username):
        return self._created_users.get(username)

    def get_created_users(self):
        return self._created_users.items()


admin = Admin("internal", "user", "admin")
admin.generate_test_users()
print(admin.get_created_users())
carl = admin.get_user("Carl Carlson")
john = admin.get_user("John Doe")

carl.say_hello_to(john)
print(carl.friends)

#11
class BaseUser:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class User(BaseUser):
    def __init__(self, *args):
        self.friends = []
        self.age_check = 10
        super().__init__(*args)

    def say_hello_to(self, user):
        err_ms = "Too much"
        if not abs(int(self.age) - int(user.age)) < age_check:
            raise ValueError(err_ms)
        self.friends.append(user)



    def __repr__(self):
        spec_str = "{}: {} {}, gender:{}, age:{}"
        return spec_str.format(self.__class__.__name__,
                               self.first_name,
                               self.last_name,
                               self.gender,
                               self.age)


class GenerateOperationsMixin:
    def get_test_names(self):
        return (('John', 'Doe', 'male', '20'),
                ('Sansa', 'Stark', 'female', '25'),
                ('Carl', 'Carlson', 'male', '15'),
                ('Thor', 'Odinson', 'male', '30'),
                ('Bruce', 'Wayne', 'male', '35'))

    def generate_test_users(self):
        for params in self.get_test_names():
            self.create_user(*params)


class Admin(GenerateOperationsMixin, User):
    _created_users = {}

    def __init__(self, first_name, last_name, position):
        self.position = position
        self.first_name = first_name
        self.last_name = last_name

    def create_user(self, *args):
        user = User(*args)
        self._created_users[user.get_name()] = user
        return user

    def get_user(self, username):
        return self._created_users.get(username)

    def get_created_users(self):
        return self._created_users.items()


admin = Admin("internal", "user", "admin")
admin.generate_test_users()
carl = admin.get_user("Carl Carlson")
bruce = admin.get_user("Bruce Wayne")
carl.say_hello_to(bruce)
print(carl.friends)

#12
class BaseUser:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class User(BaseUser):
    def __init__(self, *args):
        self.friends = []
        self.age_check = 10
        super().__init__(*args)

    def say_hello_to(self, user):
        self.check_user(user)
        self.friends.append(user)
        user.friends.append(self)

    def check_user(self, user):
        err_ms = "Too much"
        if not abs(int(self.age) - int(user.age)) < self.age_check:
            raise ValueError(err_ms)



    def __repr__(self):
        spec_str = "{}: {} {}, gender:{}, age:{}"
        return spec_str.format(self.__class__.__name__,
                               self.first_name,
                               self.last_name,
                               self.gender,
                               self.age)


class GenerateOperationsMixin:
    def get_test_names(self):
        return (('John', 'Doe', 'male', '20'),
                ('Sansa', 'Stark', 'female', '25'),
                ('Carl', 'Carlson', 'male', '15'),
                ('Thor', 'Odinson', 'male', '30'),
                ('Bruce', 'Wayne', 'male', '35'))

    def generate_test_users(self):
        for params in self.get_test_names():
            self.create_user(*params)


class Admin(GenerateOperationsMixin, User):
    _created_users = {}

    def __init__(self, first_name, last_name, position):
        self.position = position
        self.first_name = first_name
        self.last_name = last_name

    def create_user(self, *args):
        user = User(*args)
        self._created_users[user.get_name()] = user
        return user

    def get_user(self, username):
        return self._created_users.get(username)

    def get_created_users(self):
        return self._created_users.items()


admin = Admin("internal", "user", "admin")
admin.generate_test_users()
carl = admin.get_user("Carl Carlson")
john = admin.get_user("John Doe")
bruce = admin.get_user("Bruce Wayne")
carl.say_hello_to(john)
print(carl.friends)
print(john.friends)
#carl.say_hello_to(bruce)

