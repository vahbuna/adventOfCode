

def part_one():
    disp = {'n':(0,1), 's':(0,-1),
            'ne':(1, 0.5), 'se':(1, -0.5),
            'nw':(-1, 0.5), 'sw':(-1, -0.5)}
    with open('Day11.input', 'r') as dir_file:
        for line in dir_file:
            init_x = 0
            init_y = 0
            steps = 0
            farthest = 0
            for direction in line.strip().split(','):
                x, y  = disp[direction]
                init_x += x
                init_y += y
                far = abs(init_x) + abs(init_y) - 0.5*abs(init_x)
                if far > farthest:
                    farthest = far
            steps = abs(init_x) + abs(init_y) - 0.5*abs(init_x)
            print steps, farthest



if __name__ == "__main__":
    part_one()
