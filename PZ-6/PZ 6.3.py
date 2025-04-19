# Дан список A размера N и целые числа K и L (1 < K < L < N).
# Переставить в обратном порядке элементы списка, расположенные между элементами AK и AL.
# включая эти элементы.

import random

def check(type_string):
    value = input(type_string)

    while type(value) != int:
        try:
            value = int(value)
            if type(value) == int:
                return value
        except ValueError:
            print("TypeError!!!")
            value = input(type_string)



A = list()
N = check('Enter limits for list a: ')

K = check('Enter number k: ')
L = check('Enter number L: ')


for i in range(N):
    A.append(random.randint(1, 100))

print("initial value of list = ", A)

Interval = A[K:L]
Interval.reverse()
A[K:L] = Interval

print("--->sheet value after = ", A)


