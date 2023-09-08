class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return '__repr__ для объекта Car'
    def __str__(self):
        return '__str__ для объекта Car'

my_car = Car('красный', 37281)

print(my_car)
print('{}'.format(my_car))
print(str([my_car]))