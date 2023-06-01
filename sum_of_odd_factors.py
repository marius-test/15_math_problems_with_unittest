def sum_odd_factors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            sum += i
    return sum
 
if __name__ == '__main__':
    n = 11
    print(sum_odd_factors(n))

# The resulting sum includes the number itself if it is an odd number