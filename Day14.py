from itertools import cycle, islice
from collections import defaultdict

def get_knot_hash(lengths):
    c_list = range(256)
    num_elem = len(c_list)
    pos = 0
    skip = 0
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
    return dense_hash

def part_one():
    count = 0
    for i in range(128):
        input_str = 'jzgqcdpd-'+str(i)
        ascii_str = [ord(i) for i in input_str]
        for x in get_knot_hash(ascii_str):
            count += bin(int(x, 16))[2:].count('1')
    print 'answer',count

def part_two():
    regions = {}
    region = 0
    grid = []
    count = 0
    for i in range(128):
        input_str = 'jzgqcdpd-'+str(i)
        ascii_str = [ord(c) for c in input_str]
        row = []
        for x_chr in get_knot_hash(ascii_str):
            row.extend(list("{0:04b}".format(int(x_chr, 16))))
        for j, val in enumerate(row):
            if val == '1':
                if i > 0 and j > 0 and (i-1, j) in regions \
                   and (i, j-1) in regions :
                    new_val = min(regions[(i-1, j)], regions[(i, j-1)])
                    if regions[(i-1, j)] != regions[(i, j-1)]:
                        old_val = max(regions[(i-1, j)], regions[(i, j-1)])
                        for pos in regions:
                            if regions[pos] == old_val:
                                regions[pos] = new_val
                    regions[(i, j)] = new_val
                elif i>0 and (i-1,j) in regions:
                    regions[(i,j)] = regions[(i-1,j)]
                elif j>0 and (i,j-1) in regions:
                    regions[(i,j)] = regions[(i,j-1)]
                else:
                    region += 1
                    regions[(i,j)] = region
    myset = set()
    for x in regions.values():
        myset.add(x)
    print len(myset)
if __name__ == "__main__":
    part_two()
