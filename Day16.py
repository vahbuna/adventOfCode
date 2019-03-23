import re

def get_data():
    ins = []
    with open('Day16.input', 'r') as in_file:
        for line in in_file:
            ins.extend(line.strip().split(','))
    return ins

def part_two():
    cycle_one = ['a', 'd', 'i', 'n', 'c', 'e', 'h', 'g']
    cycle_two = ['b', 'f', 'k', 'm', 'p', 'j', 'l']
    inc_one = 1000000000 % 8
    inc_two = 1000000000 % 7
    input_str = list('abcdefghijklmnop')
    new_str = []
    for chrtr in input_str:
        if chrtr in cycle_one:
            idx = cycle_one.index(chrtr) + inc_one
            new_str.append(cycle_one[idx])
        elif chrtr in cycle_two:
            idx = (cycle_two.index(chrtr) + inc_two) % 7
            new_str.append(cycle_two[idx])
        else:
            new_str.append(chrtr)
    print ''.join(new_str)

def part_one():
    instructions = get_data()
    input_str = list('abcdefghijklmnop')
    old = []
    for i in range(1000000000):
        for ins in instructions:
            if ins.startswith('s'):
                pos = int(ins[1:])
                input_str = input_str[-pos:]+input_str[:-pos]
            elif ins.startswith('x'):
                pos1, pos2 = ins[1:].split('/')
                pos1 = int(pos1)
                pos2 = int(pos2)
                input_str[pos1], input_str[pos2] = input_str[pos2], input_str[pos1]
            elif ins.startswith('p'):
                prg1, prg2 = ins[1:].split('/')
                pos1 = input_str.index(prg1)
                pos2 = input_str.index(prg2)
                input_str[pos1], input_str[pos2] = input_str[pos2], input_str[pos1]
        if ''.join(input_str) in old:
            print i
            break
        else:
            old.append(''.join(input_str))


if __name__ == "__main__":
    part_one()
