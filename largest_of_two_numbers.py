def largest(a, b):
    if a > b:
        return a
    elif a == b:
        return "The numbers are equal"
    else:
        return b
    

if __name__ == '__main__':
    a = 7
    b = 59
    
    print(largest(a, b))
