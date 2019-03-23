import re
import numpy as np
from collections import defaultdict

class Program:
    name = ""
    weight = 0

    def __init__(self, name, weight):
        self.children = []
        self.name = name
        self.weight = weight

    def add_child(self, child):
        self.children.append(child)

    def has_child(self):
        return len(self.children) > 0

def sum_weights(child):
    global prg_dict
    weight_diff = 0
    weight = prg_dict[child].weight
    weights = defaultdict(list)
    weight_sum = 0
    if prg_dict[child].has_child:
        for sub_child in prg_dict[child].children:
            child_weight = sum_weights(sub_child)
            weights[child_weight].append(sub_child)
            weight_sum += child_weight
    if len(weights.keys()) > 1:
        correct_weight = 0
        wrong_weight = 0
        culprit = None
        for prg_weight, prgs in weights.iteritems():
            if len(prgs) == 1:
                wrong_weight = prg_weight
                culprit = prgs[0]
            else:
                correct_weight = prg_weight
        weight_diff = correct_weight - wrong_weight
        print child,prg_dict[culprit].weight + weight_diff, culprit
    return weight + weight_sum + weight_diff

def check_mismatch(children):
    sums = set()
    child_weights = {}
    for child in children:
        child_weight = sum_weights(child)
        sums.add(child_weight)
        child_weights[child] = child_weight
    return len(sums) != 1

def part_two():
    global prg_dict
    prg_dict = load_input()
    for prg, prg_info in prg_dict.iteritems():
        if prg_info.has_child():
            if check_mismatch(prg_info.children):
                break

# veboyvy
def part_one():
    prg_list = load_input()
    parents = set()
    children = set()
    for prg, prg_info in prg_list.iteritems():
        if prg_info.has_child():
            parents.add(prg)
            children = children.union(set(prg_info.children))
    answer = parents.difference(children)
    print len(answer), list(answer)[0]

def load_input():
    prg_table = {}
    parse_input = re.compile('([a-z]+) \(([0-9]+)\)( -> ([a-z, ]+))?')
    with open('Day07.input', 'r') as in_file:
        for line in in_file:
            data = parse_input.match(line.strip())
            name, weight_str, _, children = data.groups()
            prg = Program(name, int(weight_str))
            if children:
                for child in children.split(','):
                    prg.add_child(child.strip())
            prg_table[name] = prg
    return prg_table

if __name__ == '__main__':
    part_two()
