def nth_fibonacci_number(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect number... try again")
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b
    
    
if __name__ == '__main__':
    print(nth_fibonacci_number(5))
