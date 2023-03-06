__all__ = ["triangle_perimeter", "triangle_area"]

a, b, c = 7, 2, 8
h = 4

def triangle_perimeter(a_ = a, b_ = b, c_ = c):
    return a_ + b_ + c_

def triangle_area(a_ = a, h_ = h):
    return 0.5 * a_ * h_