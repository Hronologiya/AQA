from lesson_16.Lesson_16_2.square import Square
from lesson_16.Lesson_16_2.rectangle import Rectangle
from lesson_16.Lesson_16_2.triangle import Triangle
from lesson_16.Lesson_16_2.figure import Figure

square_f: Square = Square(10)

rectangle: Rectangle = Rectangle(10, 5)

triangle: Triangle = Triangle(5, 6, 9, 3)

figures_list: list[Figure] = [square_f, rectangle, triangle]

list_tuple_perimetr_and_square: list[tuple[int, object]] = [(figure.calculate_perimetr(), figure.calculate_square()) for figure in figures_list]

for item in list_tuple_perimetr_and_square:
    print(item[0], item[1])