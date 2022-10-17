# function definition
def simple_interest(p, r, t):
    print(f"The principal is ${p}.")
    print(f"The rate is {r}% per year.")
    print(f"The time period is {t} years.")
    return f"The amount earned is ${(p * r * t)/100}."
    
    
# this will not be run when the module is imported
if __name__ == '__main__':
    # input
    p = 1000
    r = 5
    t = 2
    
    # function call
    print(simple_interest(p, r, t))
