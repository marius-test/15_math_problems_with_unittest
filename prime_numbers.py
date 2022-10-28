def prime_numbers(a, b):
    i, j = 0, 0
    list_ = []

    for i in range(a, b + 1):
        if i == 1:
            continue

        prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                prime = False
                break

        if prime == True:
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
