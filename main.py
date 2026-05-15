def average(numbers):
    return sum(numbers) / len(numbers)


def min_max(numbers):
    return min(numbers), max(numbers)


def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Список:", numbers)

print("Середнє:", average(numbers))

minimum, maximum = min_max(numbers)
print("Мінімум:", minimum)
print("Максимум:", maximum)

print("Парні числа:", even_numbers(numbers))