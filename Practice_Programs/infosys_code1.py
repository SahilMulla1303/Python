import sys


def getMaxSubset(N,M,Two,edges,C):
    N = N
    M = M
    Two = Two
    edges = edges
    C = C
    e = []
    for i in edges:
        for j in i:
            e.append(j)

    e2 = []
    for i in range(len(e)):
        flag = 1
        for j in range(len(e)):
            if i==j :
                continue
            elif e[i] != e[j]:
                flag = flag + 1
        if flag == len(e):
            e2.append(e[i])
    result = 0
    for i in range (len(e2)):
        result = result + C[e2[i]-1]

    return result

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    Two = int(sys.stdin.readline().strip())
    edges = []
    for _ in range(M):
        edges.append(list(map(lambda x: int(x),sys.stdin.readline().strip().split(" "))))
    C = []
    for _ in range(N):
        C.append(int(sys.stdin.readline().strip()))

    result = getMaxSubset(N,M,Two,edges,C)
    print(result)

main()