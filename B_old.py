import math

def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def total_keys(x, y):
    if y % x:
        return 0

    dividers = tuple(divisor for divisor in divisor_generator(y) if not divisor % x)

    total = 0
    for num, i in enumerate(dividers):
        for j in dividers[num:]:
            if gcd(i, j) == x and lcm(i, j) == y:
                total += 2

    if x == y:
        total -= 1

    return total


if __name__ == '__main__':
    # with open("input.txt", "rt") as file:
    #     x, y = (int(i) for i in file.readline().split())
    x, y = (int(i) for i in input().split())

    print(total_keys(x, y))
