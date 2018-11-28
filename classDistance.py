class Distance:
    #случай, когда сначала объявляются метры
    @property
    def in_feet(self):
        return self.metres * 3.2808399
    
    @property
    def in_steps(self):
        return self.metres * 2
    
    @property
    def in_parsecs(self):
        return self.metres * 3.24078 * 10 ** (-17)
        
    #когда метры задаются при вызове необходимой единицы измерения
    @in_feet.setter
    def in_feet(self, metres):
        self.metres = metres
    
    @in_steps.setter
    def in_steps(self, metres):
        self.metres = metres
    
    @in_parsecs.setter
    def in_parsecs(self, metres):
        self.metres = metres

distance = Distance()
distance.metres = 1000.0
print(distance.in_feet)
print(distance.in_steps)
print(distance.in_parsecs)
distance.in_feet = 2000
print(distance.in_feet)
distance.in_steps = 54
print(distance.in_steps)
distance.in_parsecs = 1947 * 15 *20 ** 15
print(distance.in_parsecs)
