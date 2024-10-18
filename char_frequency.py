'''
Задача 3: Частота символов
Напишите функцию, которая принимает строку и возвращает словарь,
где ключами являются символы,а значениями — их частота в строке.
'''


def char_frequency(s: str) -> dict:

    """
    Args:
        s (str): строка, поданная на вход.

    Returns:
        freq_dict (dict): словарь,ключи - символы, значениями — их частота в строке s.
    """

    freq_dict = {} # Инициализируем пустой словарь для хранения частоты символов

    for char in s: # Проходим по каждому символу строки
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    return freq_dict


# Тест
string = "abracadabra"
result = char_frequency(string)
print(result)