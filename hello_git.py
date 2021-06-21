class Car:
    def __init__(self, color):
        self.color = color
    
    def getcolor(self):
        return f"{self.color}"

if __name__ == '__main__':
    my_car = Car('Blue')
    print(my_car.getcolor())