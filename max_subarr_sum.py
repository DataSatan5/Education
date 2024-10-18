'''
Задача 2: Максимальная сумма подмассива.
Напишите функцию, которая принимает список чисел и возвращает максимальную сумму подмассива.
'''

def find_max_subarray_sum(numbers: list) -> int:
    """
    Находит максимальную сумму подмассива в заданном массиве чисел.

    Args:
        numbers (list): Список целых чисел.

    Returns:
        max_sum (int): Максимальная сумма подмассива.

    Variables:
        num_len (int) : Длина массива, поданного на вход.
        max_sum (int): Максимальная сумма подмассива, найденная на текущий момент.
        curr_sum (int): Текущая сумма подмассива, которая обновляется при итерации.
    """
    num_len = len(numbers)
    max_sum = 0
    curr_sum = 0

    for _ in range(1, num_len):
        curr_sum += numbers[_]
        if (curr_sum > max_sum):
            max_sum = curr_sum
        if (curr_sum < 0):
            curr_sum = 0

    return max_sum

# Тест
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(find_max_subarray_sum(nums))  # 6 (подмассив [4,−1,2,1])