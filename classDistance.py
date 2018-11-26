class Distance:
    @property
    def other_units(self):
        self.metres = metres
        self.in_feet = self.metres * 3.2808399
        self.in_steps = self.metres * 2
        self.in_parsecs = self.metres * 3.24078 * (10 ** -17)

distance = Distance()
distance.metres = 1000.0
# футы
distance.in_feet

# шаги (допустим что в 1 метре 2 шага)
distance.in_steps

# парсеки https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D1%81%D0%B5%D0%BA
distance.in_parsecs

distance.in_feet

distance.in_feet = 200