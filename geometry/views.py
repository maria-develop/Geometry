from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample
from .serializers import (
    CircleInputSerializer,
    CircleOutputSerializer,
    TriangleInputSerializer,
    TriangleOutputSerializer,
    ShapeInputSerializer,
)
from .services import Circle, Triangle, calculate_area, create_shape


class CircleAreaView(APIView):
    @extend_schema(
        description="Вычисляет площадь круга по радиусу",
        request=CircleInputSerializer,
        responses={
            200: CircleOutputSerializer,
            400: {"description": "Неверные данные (например, радиус <= 0)"}
        },
        examples=[
            OpenApiExample(
                "Пример запроса",
                value={"radius": 5},
                request_only=True
            ),
            OpenApiExample(
                "Пример ответа",
                value={"area": 78.54},
                response_only=True
            )
        ]
    )
    def get(self, request):
        # Парсим параметры из URL: /api/geometry/circle/area/?radius=5
        radius = request.query_params.get('radius')
        if not radius:
            return Response(
                {"error": "Укажите радиус (например, ?radius=5)"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            radius = float(radius)
            circle = Circle(radius)
            return Response({"area": circle.area()})
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = CircleInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        radius = serializer.validated_data['radius']
        circle = Circle(radius)
        return Response(
            {"area": circle.area()},
            status=status.HTTP_200_OK  # Исправляем на 200 OK вместо 201 Created
        )


class TriangleAreaView(APIView):
    def post(self, request):
        serializer = TriangleInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        a = serializer.validated_data['a']
        b = serializer.validated_data['b']
        c = serializer.validated_data['c']

        try:
            triangle = Triangle(a, b, c)
            output = TriangleOutputSerializer({
                'area': triangle.area(),
                'is_right_angled': triangle.is_right_angled(),
            })
            return Response(output.data)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ShapeAreaView(APIView):
    @extend_schema(
        request=ShapeInputSerializer,
        responses={200: {"area": float}, 400: {"error": str}}
    )
    def post(self, request):
        serializer = ShapeInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            shape = create_shape(**serializer.validated_data)
            area = calculate_area(shape)
            return Response({"area": area}, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
