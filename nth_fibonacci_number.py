def nth_fibonacci_number(n):
    a = 0
    b = 1
    if n < 0:
        print("Wrong number... try again")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
    
    
if __name__ == '__main__':
    for x in range(0, 10):
        print(nth_fibonacci_number(x))
