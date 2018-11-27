class Distance:
    def __init__(self):
        self.metres = None
        
    @property
    def other_unit(self):
        self.in_feet = self.metres * 3.2808399
        self.in_steps = self.metres * 2
        self.in_parsecs = self.metres * (3.24078 ** (-17))

distance = Distance()
distance.metres = 1000.0
distance.in_feet
distance.in_steps
distance.in_parsecs
distance.in_feet = 2000
distance.in_feet
