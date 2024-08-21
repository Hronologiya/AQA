def sum_numbers_in_string(s):
    try:
        numbers = s.split(',')
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"

# Масив зі строками
strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Виводимо результат для кожного елементу списку.
results = [sum_numbers_in_string(s) for s in strings]

# Виводимо результати
for result in results:
    print(result)
