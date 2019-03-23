import numpy as np

def generator(seed, factor, multiple):
    val = seed
    while True:
        val = (val * factor) % 2147483647
        if val % multiple == 0:
            yield val

def part_two():
    a_gen = generator(116, 16807, 4)
    b_gen = generator(299, 48271, 8)
    count = 0

    for i in range(5000000):
        if bin(a_gen.next())[-16:] == bin(b_gen.next())[-16:]:
            count += 1
    print count

def part_one():
    vec = np.array([116, 299])
    count = 0
    for i in range(40000000):
        vec = np.multiply(vec, [16807, 48271]) % 2147483647
        if bin(vec[0])[-16:] == bin(vec[1])[-16:]:
            count += 1
    print count

if __name__ == "__main__":
    part_two()
