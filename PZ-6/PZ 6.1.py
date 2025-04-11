

#Сформировать и вывести целочисленный список размера 10, содержащий 10 первых
#положительных нечетных чисел: 1,3,5, ... .



def generate_odd_numbers():
    number = []
    for i in range(1,20,2):
        number.append(i)
    return number


result = generate_odd_numbers()
print(result)

