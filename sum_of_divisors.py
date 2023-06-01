def sum_divisors(n):
    divisors = [1]
    for i in range(2, n):
        if (n % i) == 0:
            divisors.append(i)
    return sum(divisors)


if __name__ == '__main__':
    n = 4
    print(sum_divisors(n))
    n = 18
    print(sum_divisors(n))
    