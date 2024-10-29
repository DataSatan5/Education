'''
Задача 2: Максимальная сумма подмассива.
Напишите функцию, которая принимает список чисел и возвращает максимальную сумму подмассива.
Реализация через алгоритм Кадане.
'''

def max_subarray_sum(nums: list) -> int:
    """
    Находит максимальную сумму подмассива в заданном массиве чисел.

    Args:
        nums (list): Список целых чисел.

    Returns:
        max_sum (int): Максимальная сумма подмассива.

    Variables:
        max_sum (int): Максимальная сумма подмассива, найденная на текущий момент.
        curr_sum (int): Текущая сумма подмассива, которая обновляется при итерации.
    """
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Тестируем
my_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(my_nums))  # 6 (подмассив [4, -1, 2, 1])
