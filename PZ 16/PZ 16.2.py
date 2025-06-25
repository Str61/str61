"""
Создайте класс "Фигура", который содержит метод расчета площади фигуры.
Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
"Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
"""


class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Shape):
    def __init__(self, side):
        super().__init__(length=side, width=side)

    def area(self):
        return self.length * self.width



class Rectangle(Shape):
    def area(self):
        return self.length * self.width


# Пример использования
square = Square(5)
print(f"Площадь квадрата: {square.area()}")  # 25

rectangle = Rectangle(4, 6)
print(f"Площадь прямоугольника: {rectangle.area()}")  # 24