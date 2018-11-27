class Distance:
    def __init__(self):
        self.metres = None
        
    @property
    def in_feet(self):
        return self.metres * 3.2808399
    @property
    def in_steps(self):
        return self.metres * 2
    @property
    def in_parsecs(self):
        return self.metres * 3.24078 * 10 ** (-17)

distance = Distance()
distance.metres = 1000.0
print(distance.in_feet)
print(distance.in_steps)
print(distance.in_parsecs)
distance.in_feet = 2000
distance.in_feet
