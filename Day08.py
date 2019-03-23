import re
from collections import defaultdict

def part_one():
    max_anytime = 0
    parse_ins = re.compile("(.+) if (.+)")
    parse_var = re.compile("[a-z]+")
    register = defaultdict(int)
    with open('Day08.input', 'r') as in_file:
        for line in in_file:
            ins, cond = parse_ins.match(line.strip()).groups()
            var_ins = parse_var.match(ins).group(0)
            var_cond = parse_var.match(cond).group(0)
            cond = cond.replace(var_cond,"register['"+var_cond+"']")
            ins = ins.replace(" inc ", " + ").replace(" dec ", " - ")
            ins = ins.replace(var_ins,"register['"+var_ins+"']")
            if eval(cond):
                register[var_ins] = eval(ins)
            max_now = register[max(register, key=register.get)]
            if max_now > max_anytime:
                max_anytime = max_now
    max_key = max(register, key=register.get)
    print max_key, register[max_key]
    print "part two", max_anytime

if __name__ == "__main__":
    part_one()
