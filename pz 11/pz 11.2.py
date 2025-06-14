# Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое, количество букв в верхнем регистре.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между первой и второй.

f2 = open("file_pz11.2.txt", "r")
l = f2.readlines()
f2.close()
count = 0
for i in l:
    print(i, end='')
    for symbol in i:
        if symbol.isupper():
            count+=1

print (f"\n\033[0;37mКол-во букв в верхнем регистре = \033[0;32m{count}\033[0;37m")

f2 = open("file_pz11_2.txt", 'w', encoding="utf-8")
for i  in l:
    if i == l[1]:
        f2.write(l[-1])
        f2.write(i)
    elif i != l[-1]:
        f2.write(i)
