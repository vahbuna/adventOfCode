import numpy as np
import re

parseRE = re.compile("p=<(.+)>,\s*v=<(.+)>,\s*a=<(.+)>")

def get_data():
    X =[]
    V =[]
    A =[]
    with open('Day20a.input', 'r') as in_file:
        for line in in_file:
            match = parseRE.match(line.strip())
            X.append([int(i) for i in match.groups()[0].split(',')])
            V.append([int(i) for i in match.groups()[1].split(',')])
            A.append([int(i) for i in match.groups()[2].split(',')])
    return (np.array(X),np.array(V),np.array(A))

def part_two():
    X, V, A = get_data()
    for k in range(3000):
        Y = X+k*V+k*(k+1)*A/2
        yu, idx = np.unique(X+k*V+k*(k+1)*A/2, return_index=True, axis=0)
        if Y.shape[0] != yu.shape[0]:
            new_X = []
            new_V = []
            new_A = []
            for ix in idx:
                answer = np.where((Y==Y[ix,]).all(axis=1))[0]
                if len(answer) == 1:
                    new_X.append(X[ix,])
                    new_V.append(V[ix,])
                    new_A.append(A[ix,])
            X = np.array(new_X)
            A = np.array(new_A)
            V = np.array(new_V)
            print X.shape[0]
            if X.shape[0] < 2:
                break

def part_one():
    X, V, A = get_data()
    for k in range(0,500000,1000):
        print np.argmin(np.sum(np.absolute(X+k*V+k*(k+1)*A/2), axis=1))

if __name__ == "__main__":
    part_two()

