import math


def fibonacci(n):
    x = 5 * n * n + 4
    s = int(math.sqrt(x))
    result = f"{n} is a Fibonacci number!" if s * s == x else f"{n} is not a Fibonacci number!"
    return result


if __name__ == '__main__':
    n = 4
    print(fibonacci(n))
