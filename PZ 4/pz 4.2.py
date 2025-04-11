#Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено
#максимально возможное количество квадратов со стороной C (без наложений).
#Найти количество квадратов, размещенных на прямоугольнике. Операции
#умножения и деления не использовать.



a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))
square = 0

while True:
    if b > 0:
        square += a
        b -= 1
    else:
        break


limit = c
mini_square = 0
while True:
    if c > 0:
        mini_square += limit
        c -= 1
    else:
        break


counter = 0
while True:
    if square > 0:
        square -= mini_square
        counter += 1
    else:
        break

print(counter)

