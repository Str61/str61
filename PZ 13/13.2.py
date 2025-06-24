#В двумерном списке отрицательные элементы возвести в квадрат.

matrix = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]

# Функциональный подход: применяем преобразование к каждому элементу
squared_matrix = list(map(
    lambda row: list(map(
        lambda x: x ** 2 if x < 0 else x,  # Возводим в квадрат только отрицательные
        row
    )),
    matrix
))

# Вывод результата
print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nМатрица после преобразования:")
for row in squared_matrix:
    print(row)