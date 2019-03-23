import re

#16827
def part_one():
    ignore_RE = re.compile('!.')
    garbage_RE = re.compile('<[^>]*>')
    with open('Day09.input', 'r') as gb_file:
        for line in gb_file:
            garbage_count = 0
            line_exclaim = ignore_RE.sub('', line.strip())
            for garbage in garbage_RE.findall(line_exclaim):
                garbage_count += len(garbage) - 2
            line_garbage = garbage_RE.sub('', line_exclaim)
            stack = []
            depth = 0
            sum_group = 0
            for c in line_garbage:
                if c == '{':
                    depth += 1
                    stack.append((c,depth))
                elif c == '}':
                    _, val = stack.pop()
                    sum_group += val
                    depth -= 1
            print sum_group, garbage_count

if __name__ == "__main__":
    part_one()
