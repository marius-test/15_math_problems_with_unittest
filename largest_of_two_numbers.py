# function definition
def largest(a, b):
    if a > b:
        return a
    elif a == b:
        return "The two numbers are equal"
    else:
        return b
    

# this will not be run when the module is imported
if __name__ == '__main__':
    # input
    a = 7
    b = 59
    
    # function call
    print(largest(a, b))
