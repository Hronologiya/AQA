#Задача 1

"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]
input_string = "Привіт Світ"
reversed_string = reverse_string(input_string)
print("Зворотний рядок:", reversed_string)

#Задача 2

def sum_of_even_numbers(numbers):
    """
    Функція, що рахує суму всіх парних чисел у списку.

    Args:
        numbers (list): Список чисел.

    Returns:
        int: Сума парних чисел у списку.
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers_list)
print(f"Сума парних чисел: {result}")

#Задача 3

def filter_strings(lst):
    """
    Функція для фільтрації рядкових елементів з заданого списку.

    :param lst: Список, який потрібно відфільтрувати
    :return: Новий список, що містить тільки рядкові елементи
    """
    return [item for item in lst if isinstance(item, str)]


list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = filter_strings(list1)

print(list2)

#Задача 4

def multiplication_table(number):
    """
    Функція друкує табличку множення на задане число,
    але лише до максимального значення для добутку - 25.

    :param number: Число для якого друкується таблиця множення.
    """
    multiplier = 1

    while multiplier <= 5:
        result = number * multiplier

        # Якщо результат більше 25, припиняємо виконання циклу
        if result > 25:
            print(f"Результат {result} перевищує 25, припиняємо виконання.")
            break

        print(f"{number}x{multiplier}={result}")

        multiplier += 1

multiplication_table(3)

# Задача 5

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:
        return 0  # Повертаємо 0, якщо список порожній
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5]
result = average(numbers)
print("Середнє арифметичне:", result)