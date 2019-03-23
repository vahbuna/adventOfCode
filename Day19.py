from collections import defaultdict

def get_data():
    data = {}
    with open('Day19.input', 'r') as in_file:
        for x, line in enumerate(in_file):
            for i, c in enumerate(list(line)):
                if c.strip():
                    data[(x,i)]=c
    return data

def part_one():
    connections = get_data()
    start = sorted(connections.keys(), key=lambda x:x[0])[0]
    # assuming  connections[start] == '|':
    next_node = (start[0]+1, start[1])
    steps = 1
    y_dir = 1
    x_dir = 0
    while next_node in connections:
        if connections[next_node] == '+':
            y_dir, x_dir = x_dir, y_dir
            if (next_node[0]+y_dir, next_node[1]+x_dir) in connections:
                next_node = (next_node[0]+y_dir, next_node[1]+x_dir)
            else:
                y_dir *= -1
                x_dir *= -1
                next_node = (next_node[0]+y_dir, next_node[1]+x_dir)
        else:
            what_next = connections[next_node]
            if what_next not in ['-', '|', '+']:
                print what_next,
            next_node = (next_node[0]+y_dir, next_node[1]+x_dir)
        steps += 1
    print steps

if __name__ == "__main__":
    part_one()
