# Zhyldyz Torogulova
# 11/5/2025

class car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color


car1 = car("Toyota Corolla", 2020, "Red")
car2 = car("Honda Civic", 2022, "Black")
car3 = car("Ford Mustang", 2018, "Blue")
# print(car1.get_model())
# print(car2.get_color())
# print(car3.fullspecs())
