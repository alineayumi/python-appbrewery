def add(*args):
    total = 0
    for number in args:
        total += number
    return total


print(add(3, 5, 6))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=2, multiply= 3)
