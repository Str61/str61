"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел.
Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

Исходные данные:
Количество элементов:
Отрицательные нечетные элементы:
Сумма отрицательных нечетных элементов:
Среднее арифметическое отрицательных нечетных элементов:
"""


# функции для удобства
def check(type_string):
    value = input(type_string)

    while type(value) != int:
        try:
            value = int(value)
            if type(value) == int:
                return value
        except ValueError:
            print("Введите целое число!!!")
            value = input(type_string)


def integer(counter):
    integer_list = list()
    for i in range(counter):
        try:
            int_user = int(check("Введите отрицательное/положительное число: "))
            # print(int_user)
            integer_list.append(int_user)

        except ValueError:
            print("Неверный ввод!!!")
    return integer_list


def f_sum_neg_int(num_list):
    sum_neg_int = 0
    for i in num_list:
        if i < 0 and not i % 2 == 0:
            sum_neg_int += i
    return sum_neg_int


def f_neg_int(num_list):
    neg_int = list()
    for i in num_list:
        if i < 0 and not i % 2 == 0:
            neg_int.append(i)
    return neg_int


# основной код программы
num = check("Введите количество символов: ")
integer_l = integer(num)
negative_num = f_neg_int(integer_l)
sum_negative_num = f_sum_neg_int(integer_l)

f1 = open("file_pz11_1.txt", 'w', encoding="UTF-8")

print(f"Исходные данные --> {integer_l}", file=f1)
print(f"Отрицательные нечётные элементы: {negative_num}", file=f1)
print(f"Сумма отрицательных нечетных элементов: {sum_negative_num}", file=f1)
print(f"Среднее арифметическое отрицательных нечетных элементов: {float(sum_negative_num / len(negative_num))}",
      file=f1)
f1.close()

print(f"\033[0;37m\nИсходные данные --> \033[1;32m{integer_l}\033[0;37m")
print(f"Отрицательные нечётные элементы: \033[1;32m{negative_num}\033[0;37m")
print(f"Сумма отрицательных нечетных элементов: \033[1;32m{sum_negative_num}\033[0;37m")
print(f"Среднее арифметическое отрицательных нечетных элементов: \033[1;32m{float(sum_negative_num / len(negative_num))}\033[1;37m")
