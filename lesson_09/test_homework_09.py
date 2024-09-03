
#Задача 1

import unittest
from homework_09 import reverse_string


class TestReverseStringFunction(unittest.TestCase):

    def test_reverse_string_positive(self):
        input_string = "Привіт Світ"
        expected_result = "тІвірпП"
        result = reverse_string(input_string)
        self.assertEqual(result, expected_result, "The string reversal is incorrect for positive test case.")

    def test_reverse_string_negative(self):
        input_string = ""  # Порожній рядок
        expected_result = ""  # Порожній рядок залишається порожнім після реверсу
        result = reverse_string(input_string)
        self.assertEqual(result, expected_result, "The string reversal is incorrect for negative test case.")


if __name__ == "__main__":
    unittest.main()

#Задача 2

import unittest
from homework_09 import sum_of_even_numbers


class TestSumOfEvenNumbers(unittest.TestCase):

    def test_positive_result_is_30(self):
        """Позитивний тест: Перевірка, що сума парних чисел дорівнює 30."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = sum_of_even_numbers(numbers)
        self.assertEqual(result, 30, f"Expected sum to be 30, but got {result}")

    def test_negative_result_not_30(self):
        """Негативний тест: Перевірка, що сума не дорівнює 30 для інших чисел."""
        numbers = [1, 2, 3]  # У цьому випадку сума парних чисел не буде дорівнювати 30
        result = sum_of_even_numbers(numbers)
        self.assertNotEqual(result, 30, f"Expected sum not to be 30, but got {result}")


if __name__ == '__main__':
    unittest.main()

#Задача 3

import unittest
from homework_09 import filter_strings


class TestFilterStrings(unittest.TestCase):
    def test_positive(self):
        list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
        expected = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']
        result = filter_strings(list1)
        self.assertEqual(result, expected)

    def test_negative(self):
        list1 = [1, 2, 3, True, False, 4.5, 6, 7, 8, 9, 0]
        expected = []
        result = filter_strings(list1)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

#Задача 4

import unittest
from io import StringIO
from unittest.mock import patch
from homework_09 import multiplication_table

class TestMultiplicationTable(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication_table_positive(self, mock_stdout):
        """
        Позитивний тест на функцію multiplication_table, перевіряє коректний вивід
        для числа 3, що не перевищує 25.
        """
        multiplication_table(3)
        # Перевірка очікуваного результату з фактичним виводом
        expected_output = "3x1=3\n3x2=6\n3x3=9\n3x4=12\n3x5=15\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output, "Тест не пройдено: вивід некоректний.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication_table_negative(self, mock_stdout):
        """
        Негативний тест на функцію multiplication_table, перевіряє вивід
        для числа 10, де результат перевищує 25.
        """
        multiplication_table(10)
        # Перевірка очікуваного результату з фактичним виводом
        expected_output = "10x1=10\n10x2=20\nРезультат 30 перевищує 25, припиняємо виконання.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output, "Тест не пройдено: вивід некоректний.")


if __name__ == "__main__":
    unittest.main()

#Задача 5

import unittest
from homework_09 import average

class TestAverageFunction(unittest.TestCase):

    def test_average_positive(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = 3.0
        result = average(numbers)
        self.assertEqual(result, expected_result, "The average calculation is incorrect for positive test case.")

    def test_average_negative(self):
        numbers = []  # Порожній список
        expected_result = 0  # Оскільки список порожній
        result = average(numbers)
        self.assertEqual(result, expected_result, "The average calculation is incorrect for negative test case.")


if __name__ == "__main__":
    unittest.main()