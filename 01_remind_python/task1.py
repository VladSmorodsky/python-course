import math


def calculate_circle_area(radius: int) -> str:
    """
    Function calculates a circle's radius

    Parameters:
        radius (int): circle radius

    Returns:
        str: circle area value or exception text
    """
    try:
        circle_radius = int(radius)
        return math.pi * circle_radius ** 2
    except ValueError:
        return 'Incorrect radius value.'
    except:
        return 'Something went wrong.'


radius_value = int(input('Enter radius value:'))

print(calculate_circle_area(radius_value))
