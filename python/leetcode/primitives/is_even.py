# write is_even w/o using mult module or division

def is_even(n):
    while n > 2:
        n -= 2
    return n == 0

# if the LSB is 0, it is an even int, else it is an odd int


def is_even_2(n):
    assert type(n) == int
    return n & 1 == 0
