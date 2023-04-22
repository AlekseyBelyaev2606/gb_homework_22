# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.
import random

list = [random.randint(0, 100) for _ in range(10)]
print(list)
list.sort()
# print(my_list)
listSorted = []
for i in list:
    if i not in listSorted:
        listSorted.append(i)
print(listSorted)