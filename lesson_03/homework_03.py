# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
"""Would you tell me, please, which way I ought to go from here?
That depends a good deal on where you want to get to, said the Cat.
I don't much care where —— said Alice.
Then it doesn't matter which way you go, said the Cat.
—— so long as I get somewhere, Alice added as an explanation.
Oh, you're sure to do that, said the Cat, if you only walk long enough.
"""
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
one_quotes = [i for i, char in enumerate(alice_in_wonderland) if char == "'"]
print(f"Символи з одинарними кавичками знаходяться на позиціях: {one_quotes}")

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

# Площа чорного моря.
area_black_sea = 436402
# Площа Азовського моря.
area_azov_sea =  37800
# Загальна площа морів.
total_see_area = area_black_sea + area_azov_sea
print(f"Чорне та азовське море разом займають площу: {total_see_area} km2")



# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items = 375291
first_and_second = 250449
second_and_third = 222950
# Знайдемо кількість товарів на другому складі.
second = second_and_third - (total_items - first_and_second)
# Знайдемо кількість товарів на першому складі.
first = first_and_second - second
# Знайдемо кількість товарів на третьому складі.
third = second_and_third - second
# Результат
print(f"Кількість товарів на першому складі: {first}")
print(f"Кількість товарів на другому складі: {second}")
print(f"Кількість товарів на третьому складі: {third}")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# Знаходимо кількість місяців
months = 12 * 1.5       # Півтора роки
monthly_payment = 1179  # грн/міс
# Розраховуемо артість комп'ютера
total_cost = monthly_payment * months
print(f"Вартість комп'ютера: {total_cost} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# Задані числа
a = 8019
b = 9907
c = 2789
d = 7248
e = 7128
f = 19224

# знаходимо остачу від діллення
remainder_a = a % 8
remainder_b = b % 9
remainder_c = c % 5
remainder_d = d % 6
remainder_e = e % 5
remainder_f = f % 9

# Результат
print(f"Остача від ділення 8019 на 8 = {remainder_a}")
print(f"Остача від ділленя 9907 на 9 = {remainder_b}")
print(f"Остача від ділення 2789 на 5 = {remainder_c}")
print(f"Остача від ділення 7248 на 6 = {remainder_d}")
print(f"Остача від ділення 7128 на 5 = {remainder_e}")
print(f"Остача від ділення 19224 на 9 = {remainder_f}")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# Данні про замовлення
items = [
    {"name": "Піцца велика", "quantity": 4, "price": 274},
    {"name": "Піцца середня", "quantity": 2, "price": 218},
    {"name": "Сік", "quantity": 4, "price": 35},
    {"name": "Торт", "quantity": 1, "price": 350},
    {"name": "Вода", "quantity": 3, "price": 21}
]
# Обчислення загальної вартості
birthday_total_cost = sum(item["quantity"] * item["price"] for item in items)
print(f"Загальна вартість замовлення: {birthday_total_cost} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos = 232 # Кількість фотографій
photos_per_page = 8 # Максимальна кількість фотографій на одній сторінці
# Обчислення необхідної кількості сторінок
pages_neded = (total_photos + photos_per_page -1) // photos_per_page

print(f"Ігорю потрібно {pages_neded} сторінок, щоб вклеїти усі фото.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance_km = 1600 #Відстань між Харковом і Будапештом.
fuel_per_100km = 9 #Витрата бензину на 100 км
tank_capacity = 48 #Місткість баку
# 1) Обчислення необхідної кількості бензину для подорожі
total_fuel_needed = (distance_km / 100) * fuel_per_100km
# 2) Обчислення кількості заправок
refuel_neded = (total_fuel_needed + tank_capacity -1) // tank_capacity

print(f"Для подорожі треба {total_fuel_needed} літрів бензину.")
print(f"Потрібно заїхати на заправку мінімум {refuel_neded} разів.")
