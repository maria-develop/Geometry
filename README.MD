Для postman

post запрос на адрес http://127.0.0.1:8000/api/geometry/circle/area/
{
  "radius": 5
}
// Ответ
{
  "area": 78.53981633974483
}


post запрос на адрес http://127.0.0.1:8000/api/geometry/triangle/area/
{
  "a": 5,
  "b": 6,
  "c": 3
}
// Ответ
{
    "area": 7.483314773547883,
    "is_right_angled": false
}


post запрос на адрес http://127.0.0.1:8000/api/geometry/shape/area/
{
    "shape_type": "circle",
    "radius": 5
}
// Ответ
{
    "area": 78.53981633974483
}