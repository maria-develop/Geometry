from .models import Shape
from typing import Union
import math


class Circle(Shape):
    """Класс для представления круга."""

    def __init__(self, radius: float):
        """
        Инициализирует круг с заданным радиусом.

        :param radius: Радиус круга (должен быть положительным)
        :raises ValueError: Если радиус отрицательный или нулевой
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        """Вычисляет площадь круга по формуле πr²."""
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> None:
        """Для круга понятие прямоугольности не применимо."""
        return None


class Triangle(Shape):
    """Класс для представления треугольника."""

    def __init__(self, a: float, b: float, c: float):
        """
        Инициализирует треугольник с заданными сторонами.

        :param a: Длина первой стороны
        :param b: Длина второй стороны
        :param c: Длина третьей стороны
        :raises ValueError: Если стороны не могут образовать треугольник
        """
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Длины сторон должны быть положительными")

        sides_sorted = sorted(sides)
        if sides_sorted[0] + sides_sorted[1] <= sides_sorted[2]:
            raise ValueError("Сумма длин любых двух сторон должна быть больше третьей")

        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Вычисляет площадь треугольника по формуле Герона."""
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_angled(self) -> bool:
        """Проверяет, является ли треугольник прямоугольным по теореме Пифагора."""
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)


def create_shape(**kwargs) -> Union[Circle, Triangle]:
    """Фабричный метод для создания фигур."""
    shape_type = kwargs.pop('shape_type')  # Извлекаем тип фигуры

    if shape_type == 'circle':
        return Circle(radius=kwargs['radius'])
    elif shape_type == 'triangle':
        return Triangle(a=kwargs['a'], b=kwargs['b'], c=kwargs['c'])
    else:
        raise ValueError(f"Неизвестный тип фигуры: {shape_type}")


def calculate_area(shape: Shape) -> float:
    """Вычисляет площадь фигуры через полиморфизм."""
    return shape.area()
