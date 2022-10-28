def prime_numbers(a, b):
    i, j, prime = 0, 0, 0
    list_ = []

    for i in range(a, b + 1):
        if i == 1:
            continue

        prime = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                prime = 0
                break

        if prime == 1:
            list_.append(i)
            print(i, end=" ")
    return list_

if __name__ == '__main__':
    print("Enter lower bound of the interval: ", end="")
    a = int(input())
    print(a)

    print("Enter upper bound of the interval: ", end="")
    b = int(input())
    print(b)

    print("Prime numbers between", a, "and", b, "are: ", end="")
    
    prime_numbers(a, b)
