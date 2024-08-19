# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b

# Приклад використання:
result = sum_two_numbers(3, 5)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:
        return 0  # Повертаємо 0, якщо список порожній
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5]
result = average(numbers)
print("Середнє арифметичне:", result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]
input_string = "Привіт Світ"
reversed_string = reverse_string(input_string)
print("Зворотний рядок:", reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    if not words:
        return ""  # Повертаємо порожній рядок, якщо список порожній
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Приклад використання
words_list = ["груша", "слива", "абрикос", "фасолька"]
result = longest_word(words_list)
print("Найдовше слово:", result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index =str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def calculate_total_sea_area(area_black_sea, area_azov_sea):
    """
    Обчислює загальну площу Чорного та Азовського морів.

    Parameters:
    area_black_sea (int): Площа Чорного моря в квадратних кілометрах.
    area_azov_sea (int): Площа Азовського моря в квадратних кілометрах.

    Returns:
    int or float: Загальна площа морів в квадратних кілометрах.
    """
    total_sea_area = area_black_sea + area_azov_sea
    return total_sea_area

# Використання функції
area_black_sea = 436402  # Площа Чорного моря
area_azov_sea = 37800    # Площа Азовського моря

total_area = calculate_total_sea_area(area_black_sea, area_azov_sea)
print(f"Чорне та Азовське море разом займають площу: {total_area} km²")

# task 8
def has_more_than_ten_unique_chars(user_input):
    """
    Перевіряє, чи містить рядок більше 10 унікальних символів.

    Parameters:
    user_input (str): Рядок, який потрібно перевірити.

    Returns:
    bool: True, якщо у рядку більше 10 унікальних символів, інакше False.
    """
    unique_chars = set(user_input)
    return len(unique_chars) > 10

# Виклик функції з параметром
print(has_more_than_ten_unique_chars(input("Введіть рядок: ")))

# task 9
def prompt_for_word_with_h():
    """
    Вимагає від користувача ввести слово, яке містить літеру 'h' (враховуються як великі, так і маленькі літери).
    Цикл не завершиться, поки користувач не введе правильне слово.

    Returns:
    str: Слово, яке містить літеру 'h'.
    """
    while True:
        user_input = input("Введіть слово: ")
        if 'h' in user_input.lower():
            return user_input
        else:
            print("Слово повинно містити літеру 'h'. Спробуйте ще раз!")

# Виклик функції
word_with_h = prompt_for_word_with_h()
print(f"Ви ввели слово з літерою 'h': {word_with_h}")

# task 10

def filter_strings_from_list(input_list):
    """
    Формує новий список, який містить лише змінні типу стрінг з вхідного списку.

    Parameters:
    input_list (list): Вхідний список, який може містити змінні різних типів.

    Returns:
    list: Новий список, який містить лише змінні типу стрінг.
    """
    return [item for item in input_list if isinstance(item, str)]

# Виклик функції з параметром
list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = filter_strings_from_list(list1)
print(list2)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""