'''
Задача 1: Реверсирование строки
Напишите функцию, которая принимает строку и возвращает её, но со словами в обратном порядке.
'''

def reverse_words(my_str: str) -> str:
    '''
    Функция разворачивает порядок слов в строке, поданной на вход.

    Args:
        Строка my_str (str).

    Returns:
        new_str (str): развернутая строка.
    '''
    new = ' '.join(my_str.split()[::-1])

    return new


# Тест
s = "Hello world from Python"
print(reverse_words(s))  # "Python from world Hello"
print(type(reverse_words(s))) # <class 'str'>