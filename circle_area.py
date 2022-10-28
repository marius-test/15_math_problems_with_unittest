import math


def circle_area(r):
    pi = math.pi
    a = pi * r ** 2
    a = round(a, 2)
    print(f'The area of a circle with the radius equal to {r} is ~ {a}.')
    return a

if __name__ == '__main__':
    r = 5
    circle_area(r)
    