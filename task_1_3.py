import geometry
from geometry import circle_area
from geometry.flat import triangle_area

print("1. geometry.circle_area(5) =", geometry.circle_area(5))
print("2. circle_area(5)         =", circle_area(5))
print("3. triangle_area(3, 4)    =", triangle_area(3, 4))
print("4. geometry.sphere_volume(2) =", geometry.sphere_volume(2))
print("geometry.__file__         =", geometry.__file__)