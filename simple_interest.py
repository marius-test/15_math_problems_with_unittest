def simple_interest(p, r, t):
    print(f"The principal is ${p}.")
    print(f"The rate is {r}% per year.")
    print(f"The time period is {t} years.")
    print(f"The amount earned is ${(p * r * t)/100}")
    return (p * r * t)/100


if __name__ == '__main__':
    p = 1000
    r = 5
    t = 2

    simple_interest(p, r, t)
