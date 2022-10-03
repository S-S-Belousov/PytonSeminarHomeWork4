# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from function import get_non_repeating_elements as get_elements
from function import get_random_list

my_len_list = int(input('Введите количество элементов списка: '))
my_min_list = int(input('Введите минимальный элемент списка: '))
my_max_list = int(input('Введите максимальный элемент списка: '))
my_rand_list = get_random_list(my_len_list, my_min_list, my_max_list)
print(f'Сгенерированный список:\n{my_rand_list}')
print(f'Список неповторяющихся элементов:\n{get_elements(my_rand_list)}')