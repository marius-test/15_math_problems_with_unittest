def sum_of_cubes(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i * i
    return result


if __name__ == '__main__':
    n = 2
    print(sum_of_cubes(n))
