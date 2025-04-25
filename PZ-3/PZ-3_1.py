#Дано целое число A. Проверить истинность высказывания: «Число A является
#положительным».

def check(string):
    a = input(string)
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print("Ведите целое число!")
            a = int(input(string))
        return a


num_user = check("Введите положительное число:")
if num_user > 0:
    print("Число положительное - верно")
else:
    print("Число отрицательное - не верно")