def sum_of_squares(n):
    result = 0
    for i in range(1, n + 1):
        result = result + (i * i)
    return result


if __name__ == '__main__':
    n = 4
    print(sum_of_squares(n))
