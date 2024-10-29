import timeit

'''
Задача 3*: Максимальная сумма подмассива.
Напишите функцию, которая принимает список чисел и возвращает максимальную сумму подмассива.
>> Сравнить реализацию через цикл и алгоритма Кадане.
'''

def max_subarray_sum_loop(nums: list) -> int:
    num_len = len(nums)
    max_sum = 1e-8
    curr_sum = 0

    for _ in range(num_len):
        curr_sum += nums[_]
        if (curr_sum > max_sum):
            max_sum = curr_sum
        if (curr_sum < 0):
            curr_sum = 0

    return max_sum

def max_subarray_sum_kadane(nums: list) -> int:
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Тест производительности.

my_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

time1 = timeit.timeit(lambda: max_subarray_sum_loop(my_nums), number=1000000)
time2 = timeit.timeit(lambda: max_subarray_sum_kadane(my_nums), number=1000000)
print(f"Время выполнения через цикл = {round(time1, 3)}, через алгоритм Кадане = {round(time2, 3)}.")
print(f"Разница в быстродействии: в {round(time2/time1, 3)} раз(а)")
