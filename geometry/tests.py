import unittest
import math
from services import Circle, Triangle, calculate_area


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # Не выполняется неравенство треугольника

    def test_right_angled_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_angled())
        self.assertTrue(Triangle(5, 12, 13).is_right_angled())
        self.assertFalse(Triangle(3, 4, 6).is_right_angled())

    def test_calculate_area_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(shape) for shape in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)

    def test_circle_is_right_angled(self):
        self.assertIsNone(Circle(5).is_right_angled())


if __name__ == '__main__':
    unittest.main()
