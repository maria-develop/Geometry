from django.urls import path
from .views import CircleAreaView, TriangleAreaView, ShapeAreaView


urlpatterns = [
    path('circle/area/', CircleAreaView.as_view(), name='circle-area'),
    path('triangle/area/', TriangleAreaView.as_view(), name='triangle-area'),
    path('shape/area/', ShapeAreaView.as_view(), name='shape-area'),
]

