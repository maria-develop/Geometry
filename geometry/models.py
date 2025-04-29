from django.db import models
from abc import ABC, abstractmethod
from typing import Optional


class Shape(ABC):
    """Абстрактный базовый класс для геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass

    @abstractmethod
    def is_right_angled(self) -> Optional[bool]:
        """
        Проверяет, является ли фигура прямоугольной (если применимо).
        Возвращает None для фигур, где это не имеет смысла.
        """
        pass


class Calculation(models.Model):
    """модели Django для хранения результатов"""
    shape_type = models.CharField(max_length=20)
    parameters = models.JSONField()
    area = models.FloatField()
    is_right_angled = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shape_type} calculation"
