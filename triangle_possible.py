def triangle_possible(a, b, c):
    if a != 0 and b != 0 and c != 0 and a + b + c == 180:
        if a + b >= c or b + c >= a or a + c >= b:
            return "Triangle possible with the given angles!"
        else:
            return "Triangle not possible with the given angles!"
    else:
        return "Triangle not possible with the given angles!"
 

if __name__ == '__main__':
    a, b, c = 50, 60, 70
    print(triangle_possible(a, b, c))
    