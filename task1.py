import math


def calculate_circle_area(radius):
    try:
        circle_radius = int(radius)
        return math.pi * circle_radius ** 2
    except ValueError:
        return 'Incorrect radius value.'


radius_value = input('Enter radius value:')

print(calculate_circle_area(radius_value))
