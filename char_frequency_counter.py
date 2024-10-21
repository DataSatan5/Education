'''
Задача 3: Частота символов
Напишите функцию, которая принимает строку и возвращает словарь,
где ключами являются символы,а значениями — их частота в строке.
'''

from collections import Counter

def char_frequency(s: str) -> dict:
    """
    Args:
        s (str): строка, поданная на вход.

    Returns:
        dict: словарь,ключи - символы, значениями — их частота в строке s.
    """
    return dict(Counter(s))

# Тест
string = "hello world"
result = char_frequency(string)
print(result)