import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

new_text = adwentures_of_tom_sawer.replace("\n", " ")
print(new_text)

# task 02 ==
""" Замініть .... на пробіл
"""
new_text = new_text.replace("....", " ")
print(new_text)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
new_text = new_text.replace("  "," ")
print(new_text)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
character_h_couunt = adwentures_of_tom_sawer.count('h')
print(f"Літера 'h' зустрічаеться {character_h_couunt} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
capitalized_word_count = sum(1 for word in words if word.istitle())
print(f"Кількість слів, що починаються з великої літери: {capitalized_word_count}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_occurance = new_text.find('Tom')
second_occurance = new_text.find('Tom', first_occurance + 1)
print(f"Слово 'Tom' зустрічаеться на позиції {second_occurance}.")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?]) +', new_text)
print(new_text)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
    print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        found = True
        break

if found:
    print("Є речення, яке починається зі слів 'By the time'.")
else:
    print("Немає речень, які починаються зі слів 'By the time'.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentance = adwentures_of_tom_sawer_sentences[-1]
words_count = len(last_sentance.split())
print(f"Останнє речення: {last_sentance}")
print(f"Кількість слів в останньому реченні: {words_count}")