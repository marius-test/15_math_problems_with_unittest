# function definition
def compound_interest(p, r, t):
    print(f"The principal is ${p}.")
    print(f"The rate is {r}% per year.")
    print(f"The time period is {t} years.")
    a = round((p * (1 + r/100) ** t), 2)
    print(f"The amount earned is ${a}")
    return a
    
    
# this will not be run when the module is imported
if __name__ == '__main__':
    # input
    p = 1000
    r = 5
    t = 2
    
    # function call
    compound_interest(p, r, t)
    