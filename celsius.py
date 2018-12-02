class Celsius:
    #дескриптор для перевода графусов по Фаренгейту в градусы по Цельсию
    def __get__(self, instance, owner):
        instance.celsius = (instance.fahrenheit - 32) * 5 / 9
        return instance.celsius

class Temperature:

    celsius = Celsius()

    def __init__(self, initial):
        self.fahrenheit = initial
        
temp1, temp2, temp3 = Temperature(15), Temperature(150), Temperature(-100)
print('15F = {},\n150F = {},\n-100F = {}'.format(temp1.celsius, temp2.celsius, temp3.celsius))
