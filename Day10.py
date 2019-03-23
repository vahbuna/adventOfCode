from itertools import cycle, islice

def get_lengths():
    with open('Day10.input', 'r') as l_file:
        for line in l_file:
            return [int(i.strip()) for i in line.strip().split(',')]

def get_length_ascii():
    with open('Day10.input', 'r') as l_file:
        for line in l_file:
            return [ord(i) for i in line.strip()]


def part_one():
    lengths = get_lengths()
    c_list = range(256)
    num_elem = len(c_list)
    pos = 0
    skip = 0
    for l in lengths:
        y = pos
        for a in reversed(list(islice(cycle(c_list), pos, pos+l))):
            c_list[ y % num_elem] =a
            y += 1
        pos += l+skip
        skip += 1
    print c_list[0] * c_list[1]

def part_two():
    c_list = range(256)
    num_elem = len(c_list)
    pos = 0
    skip = 0
    lengths = get_length_ascii()
    lengths += [17, 31, 73, 47, 23]
    for i in range(64):
        for l in lengths:
            y = pos
            for a in reversed(list(islice(cycle(c_list), pos, pos+l))):
                c_list[ y % num_elem] =a
                y += 1
            pos += l+skip
            skip += 1
    dense_hash = ''
    for i in range(16):
        hex_num = reduce(lambda x,y : x^y,
                   list(islice(c_list, i*16, (i+1)*16)))
        dense_hash += "{0:0{1}x}".format(hex_num,2)
    print dense_hash

if __name__ == "__main__":
    part_two()
