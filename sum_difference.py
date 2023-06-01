def sum_difference(n):
    sum_of_squares = 0
    square_of_sum = 0
    
    for num in range(1, n + 1):
        square_of_sum = square_of_sum + num
        sum_of_squares = sum_of_squares + (num * num)

    square_of_sum = square_of_sum ** 2

    return square_of_sum - sum_of_squares

if __name__ == '__main__':
    n = 10
    print(sum_difference(n))