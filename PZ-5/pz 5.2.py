# Описать функцию PowerA234(параметры), вычисляющую вторую, третью и
# четвертую степень числа A и возвращающую эти степени соответственно в
# переменные B, C и D. С помощью этой функции найти вторую, третью и четвертую
# степень пяти данных чисел.

def numbr(a):
    return a ** 2, a ** 3, a ** 4


nmbrs = int(input("Inter a number: "))
b, c, d = numbr(nmbrs)
print(b, c, d)


