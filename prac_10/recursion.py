"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)



do_something(4)

def pyramid(n):
    blocks = 0
    for number in range(0,n+1):
        blocks += number
    print(blocks)

pyramid(6)

def pyramid_scheme(n, blocks=0):
    if n > 0:
        blocks += n
        pyramid_scheme(n-1, blocks)
    else:
        print(blocks)

pyramid_scheme(6)
