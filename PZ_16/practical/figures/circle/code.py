__all__ = ["circle_perimeter", "circle_area"]

default_radius = 5
pi = 3.14

def circle_perimeter(radius = default_radius):
    return 2 * pi * radius

def circle_area(radius = default_radius):
    return pi * pow(radius, 2)