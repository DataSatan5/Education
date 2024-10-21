'''
Задача 3*: Частота символов (разные реализации)
Напишите функцию, которая принимает строку и возвращает словарь,
где ключами являются символы,а значениями — их частота в строке.
>> Сравнить реализацию через цикл и counter(collections).
'''
import timeit
from collections import Counter

def char_frequency_counter(s: str) -> dict:
    return dict(Counter(s))

def char_frequency_loop(s: str) -> dict:
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

# Тест производительности.

my_string = "hello world, piano" * 100

time1 = timeit.timeit(lambda: char_frequency_counter(my_string), number=10000)
time2 = timeit.timeit(lambda: char_frequency_loop(my_string), number=10000)
print(f"Время выполнения через Counter = {round(time1, 3)}, через цикл = {round(time2, 3)}.")
print(f"Разница в быстродействии: в {round(time2/time1, 2)} раз(а)")