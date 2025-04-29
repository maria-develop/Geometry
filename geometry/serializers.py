from rest_framework import serializers


class CircleInputSerializer(serializers.Serializer):
    radius = serializers.FloatField(
        min_value=0.01,
        help_text="Радиус круга (должен быть положительным)"
    )


class CircleOutputSerializer(serializers.Serializer):
    area = serializers.FloatField(help_text="Площадь круга")


class TriangleInputSerializer(serializers.Serializer):
    a = serializers.FloatField(min_value=0.01)
    b = serializers.FloatField(min_value=0.01)
    c = serializers.FloatField(min_value=0.01)


class TriangleOutputSerializer(serializers.Serializer):
    area = serializers.FloatField()
    is_right_angled = serializers.BooleanField()


class ShapeInputSerializer(serializers.Serializer):
    shape_type = serializers.ChoiceField(choices=['circle', 'triangle'])

    # Параметры для круга
    radius = serializers.FloatField(required=False, min_value=0.01)

    # Параметры для треугольника
    a = serializers.FloatField(required=False, min_value=0.01)
    b = serializers.FloatField(required=False, min_value=0.01)
    c = serializers.FloatField(required=False, min_value=0.01)

    def validate(self, data):
        """Проверяем, что переданы правильные параметры для фигуры."""
        shape_type = data['shape_type']

        if shape_type == 'circle':
            if 'radius' not in data:
                raise serializers.ValidationError("Для круга требуется радиус")
        elif shape_type == 'triangle':
            for side in ['a', 'b', 'c']:
                if side not in data:
                    raise serializers.ValidationError(f"Для треугольника требуется сторона {side}")

        return data
