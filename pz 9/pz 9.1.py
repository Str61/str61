# Используя словарь посчитать количество уникальных слов в заданном предложении «Изучаем язык Питон».
# Вывести на экран каждую пару «ключ:значение».


string = "Изучаем язык Питон"
list_str = string.split()
tytyty_list = dict()
counter_keys = 0

for i in list_str:
    if i not in tytyty_list:
        tytyty_list[i] = 1
        counter_keys += 1
    else:
        tytyty_list[i] += 1

print("Количество повторений уникальных слов:")
for i in tytyty_list.items():
    print(i)

print(f"Количество уникальных слов: {counter_keys}")