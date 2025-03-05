b = int(input("Введите любое положительное число: "))
a = int(input("Введите любое положительное число: "))
while a<0:
    if a < 0:
        print("Вы ввели отрицательное число!")
        a = int(input("Введите повторно положительное число: "))
        print(a)
    else:
        break

while b<0:
    if b < 0:
        print("Вы ввели отрицательное число!")
        b = int(input("Введите повторно положительное число: "))
        print(b)
    else:
        break
p = 0

for i in range(a,b+1):
    print(i)
    p+=1


print(p)