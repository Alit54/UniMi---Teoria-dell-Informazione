import math

def H_SR(C: list[list[float]], P: list[float]) -> float:
    if len(C) != len(P):
        raise Exception('Lenght are not correct')
    entropy = 0
    for x in range(len(C)):
        for y in range(len(C[x])):
            p_y = sum([C[xx][y]*P[xx] for xx in range(len(C))])
            p_xy = M[x][y]*P[x]
            entropy += p_xy*math.log(p_y/p_xy,2)
    return entropy
                

def H_RS(C: list[list[float]], P: list[float]) -> float:
    if len(C) != len(P):
        raise Exception('Lenght are not correct')
    entropy = 0
    for x in range(len(C)):
        for y in range(len(C[x])):
            entropy += M[x][y]*P[x]*-math.log(M[x][y], 2)
    return entropy

if __name__ == '__main__':
    M = [
        [0.2, 0.2, 0.3, 0.2, 0.1],
        [0.2, 0.5, 0.1, 0.1, 0.1],
        [0.6, 0.1, 0.1, 0.1, 0.1],
        [0.3, 0.1, 0.1, 0.1, 0.4]
        ]
    P = [0.2, 0.3, 0.1, 0.4]
    print(H_RS(M, P))
    print(H_SR(M, P))