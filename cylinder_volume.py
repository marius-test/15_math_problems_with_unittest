import math

def cylinder_volume(r, h):
    if r > 0 and h > 0:
        V = math.pi * r ** 2 * h
        V = round(V, 2)
        return f"The volume of the cylinder is {V}."
    else:
        return "Please input positive numbers!"

if __name__ == '__main__':
    r = 3
    h = 6
    
    print(cylinder_volume(r, h))