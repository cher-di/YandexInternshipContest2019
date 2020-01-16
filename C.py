def num_of_ones(n):
    xor = bin(n)
    counter = 0
    for i in xor:
        if i == '1':
            counter += 1
    return counter


def min_a_xor(a):
    n = len(a)

    a = sorted(a)

    min_distance = a[-1] - a[0]
    second_distance = min_distance
    for k in range(n - 1):
        new_distance = a[k + 1] - a[k]
        if new_distance < min_distance:
            second_distance = min_distance
            min_distance = new_distance
        else:
            if new_distance < second_distance:
                second_distance = new_distance
        if not min_distance:
            return 0

    min_xor = 10 ** 9
    for k in range(n - 1):
        if a[k + 1] - a[k] in (min_distance, second_distance):
            min_xor = min(min_xor, a[k] ^ a[k + 1])

    return min_xor


if __name__ == '__main__':
    with open("input.txt", "rt") as file:
        T = int(file.readline().split()[0])
        for i in range(T):
            n = int(file.readline().split()[0])
            a = tuple(int(i) for i in file.readline().split())

            print(min_a_xor(a))
