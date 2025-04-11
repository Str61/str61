#Дан список размера N. Найти номера тех элементов списка, которые больше своего
#правого соседа, и количество таких элементов. Найденные номера выводить в
#порядке их возрастания.

def spisok(numbers):
    indices = list()
    count = 0
    for i in range(0, len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            print("-----")
            indices.append(numbers.index(i))
            count += 1
        return indices, count


numbers = [1,5,2,8,3,7,4]
result_indices,result_count = spisok(numbers)
print("Номера элементов:", result_indices)
print("Количество:",result_count)