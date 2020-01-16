def get_primes(border: int) -> list:
    primes = [2]
    for i in range(3, border + 1, 2):
        for prime in primes:
            if not i % prime:
                break
        else:
            primes.append(i)
    return primes


def get_prime_divisors(num: int, primes) -> list:
    prime_divisors = []
    for prime in primes:
        if prime > num:
            break
        if not num % prime:
            prime_divisors.append(prime)
    return prime_divisors


def get_divisors_power(num: int, prime_divisors: iter) -> dict:
    powers = {prime: 0 for prime in prime_divisors}
    for prime in prime_divisors:
        while not num % prime:
            num = num // prime
            powers[prime] += 1
    return powers


if __name__ == '__main__':
    x, y = (int(i) for i in input().split())
    if y % x:
        print(0)
    elif x == y:
        print(1)
    else:
        y_div_x = y // x
        max_value = max(x, y_div_x)
        primes = get_primes(max_value)
        prime_divisors_x = get_prime_divisors(x, primes)
        prime_divisors_y_div_x = get_prime_divisors(y_div_x, primes)

        prime_divisors = set(prime_divisors_x + prime_divisors_y_div_x)
        x_powers = get_divisors_power(x, prime_divisors)
        y_powers = get_divisors_power(y, prime_divisors)
        n = 0
        for prime in prime_divisors:
            if x_powers[prime] != y_powers[prime]:
                n += 1
        print(2 ** n)
