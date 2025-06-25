"""
Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
площади, длины окружности и диаметра.
"""

class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def square(self):
        return self.radius * self.radius * 3.14

    def size(self):
        return self.radius * 6.28

    def diameter(self):
        return self.radius * 2



# Пример использования
my_circle = Circle(10)

print(f"Радиус - {my_circle.radius}\nПлощадь {my_circle.square()}\n"
      f"Длина окружности - {my_circle.size()}\nДиаметр - {my_circle.diameter()}")